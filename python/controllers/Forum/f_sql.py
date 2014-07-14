# __author__ = 'ming'
#coding=utf-8



SBig_sql = """
              select
                a.*,
                (select u_name from sys_user where u_tid=a.bb_admin) as bb_who,
                (select sum(bs.bs_postCount)  from t_forum_boards_small bs where bs.bs_bigID=a.bb_tid) as bb_postCount ,
                (select sum(bs.bs_replyCount) from t_forum_boards_small bs where bs.bs_bigID=a.bb_tid) as bb_replyCount

                from t_forum_boards_bigs a
            """
