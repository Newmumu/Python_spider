from redis import Redis
import time

conn = Redis(host='127.0.0.1', port=6379)

ONE_WEEK_IN_SECONDS = 7 * 24 * 3600  # 一篇文章有效的点赞时间段为：发布后的一周内
VOTE_SCORE = 432  # 每天共86400秒，如果一篇文章点赞超过了200票，就认为有趣，展示在首页1天 故 86400/200


def article_vote(conn, user, article):
    """文章投票（后续加入事务处理能力）"""
    cutoff = time.time() - ONE_WEEK_IN_SECONDS
    if conn.zscore('time:', article) < cutoff:
        return
    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)


def post_article(conn, user, title, link):
    """发布新文章功能实现"""
    article_id = str(conn.incr('article:'))

    voted = 'voted:' +article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
    })
    conn.zadd('score:', article, now+VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id


ARTICLES_PER_PAGE = 25


def get_articles(conn, page, order='score:'):
    """取出评分最高的文章，和取出最新的文章"""
    start = (page-1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    ids = conn.zrevrange(order, start, end)
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles


def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    """构建群组，进行特定话题展示！  将文章加入到群组和从群组中移除文章的功能实现"""
    article = 'article:' + article_id
    for group in to_add:
        conn.sadd('group:' + group, article)
    for group in to_remove:
        conn.srem('group:' + group, article)

    pass


def get_group_articles(conn, group, page, order='score:'):
    """重用 get_articles函数，实现从群组中获取一整页文章的方法"""
    key = order + group
    if not conn.exists(key):
        conn.zinterstore(key,
                         ['group:' + group, order],
                         aggregate='max',
                        )
        conn.expire(key, 60)  # 让redis 在60秒后，自动删除这个有序集合
    return get_articles(conn, page, key)


def check_token(conn, token):
    """尝试获取并返回令牌"""
    return conn.hget('login:', token)


pass
