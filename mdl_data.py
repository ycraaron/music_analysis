# encoding = utf-8
# name = mdl_date.py
# Author: Aaron Yang
# 2016.07.03
import mdl_db_manager


class MdlData(object):

    def __init__(self):
        self.db_connection = mdl_db_manager.MdlDatabase()
        self.ls_course_id = []              # store the all the id for the course which contains block learning_analysis
        self.ls_log_tmp = []                # store the tmp log info we need
        self.ls_log = []                    # store the log info
        self.ls_course_elo = []             # store how many elos does a course have, e.g: elo 1,2,3...
        self.ls_elo_component = []          # store the component for each single elo
        self.ls_student_tmp = []            # store student information for every calculation
        self.ls_student = []                # store the calculated result
        self.ls_forum_id = []               # store the forum id result
        self.ls_forum_component_id = []
        self.ls_ouwiki_component_id = []
        self.ls_posts = []

    def is_connected(self):
        return self.db_connection.is_connected()

    def update(self, target, params=[]):
        if target == "ue_mapping":
            self.db_connection.clear_data("TRUNCATE TABLE `mdl_elo_ue_mapping`")
            sql = "INSERT INTO `mdl_elo_ue_mapping` (`user_id`, `user_name`, `course_id`, `elo_id`, `engagement`) VALUES (%s, %s, %s, %s, %s) "
            return self.db_connection.insert_data(sql, params)

        elif target == "uc_mapping":
            self.db_connection.clear_data("TRUNCATE TABLE `mdl_elo_uc_mapping`")
            sql = "INSERT INTO `mdl_elo_uc_mapping` (`user_id`, `user_name`, `course_id`, `elo_id`, `component_id`, `component_name`, `engagement`) VALUES (%s, %s, %s, %s, %s, %s, %s) "
            return self.db_connection.insert_data(sql, params)

        # update norm weight
        elif target == "ec_mapping":
            self.db_connection.clear_data("TRUNCATE TABLE `mdl_elo_ec_mapping`")
            sql = "INSERT INTO `mdl_elo_ec_mapping` (`course_id`,`elo_id`,`component_id`,`component_name`,`avg_engagement`) VALUES (%s, %s, %s, %s, %s) "
            return self.db_connection.insert_data(sql, params)

        elif target == "elo_component":
            sql = "UPDATE `mdl_elo_component` SET `weight` = %s WHERE `id` = %s"
            return self.db_connection.update_data(sql, params)
        elif target == "forum_post_relation":
            self.db_connection.clear_data("TRUNCATE TABLE `mdl_elo_forum_post_relation`")
            sql = "INSERT INTO `mdl_elo_forum_post_relation` (`post_id`,`user_from_id`,`user_from_name`,`user_to_id`,`user_to_name`,`forum_id`,`forum_component_id`) VALUES (%s, %s, %s, %s, %s, %s, %s) "
            return self.db_connection.insert_data(sql, params)
        elif target == "unique_relation":
            self.db_connection.clear_data("DELETE FROM `mdl_elo_forum_relation_stats`")
            sql = "INSERT IGNORE INTO `mdl_elo_forum_relation_stats` (`user_from_id`,`user_from_name`,`user_to_id`,`user_to_name`,`forum_component_id`, `total_post_count`) VALUES(%s, %s, %s, %s, %s, %s)"
            return self.db_connection.insert_data(sql, params)
        elif target == "relation_stats_sql":
            sql = "UPDATE mdl_elo_forum_relation_stats AS a SET a.total_post_count = (SELECT COUNT(*) FROM mdl_elo_forum_post_relation AS b WHERE a.user_from_id = b.user_from_id AND a.user_to_id = b.user_to_id AND a.forum_component_id = b.forum_component_id)"
            return self.db_connection.update_data(sql)
        elif target == "relation_stats":
            sql = "UPDATE mdl_elo_forum_relation_stats AS a SET a.total_post_count = %s WHERE a.user_from_id = %s AND a.user_to_id = %s AND a.forum_component_id = %s"
            return self.db_connection.update_data(sql, params)
        elif target == "score_prediction":
            #print params
            sql = "REPLACE INTO mdl_sp_result (userid, courseid, cnt_viewcoursesection,cnt_viewforums,cnt_viewurls,cnt_submitassign," \
                  "cnt_quizclose,cnt_quizstart,cnt_quizcontinue,cnt_wikiedit,cnt_viewsubmitassign,predicted_score) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            return self.db_connection.insert_data(sql, params)
        else:
            sql = "UPDATE `mdl_elo_info` SET `avg_engagement` = %s WHERE `course` = %s AND elo = %s"
            return self.db_connection.update_data(sql, params)

    def update_music_type(self, params):
        sql = "REPLACE into sub_music_type(subject, empty,blues,classical,country,easylistening,electronic,folk," \
            "holiday,international,jazz,latin,newage,poprock,rb,stagescreen) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self.db_connection.update_data(sql, params)

    def update_act_stats(self, param, column_name):

        sql = "UPDATE sub_actv_genre_stats SET "+column_name+" = %s WHERE subject = %s AND activity = %s"
        return self.db_connection.update_data(sql,param)

    def update_act_song_mood_stats(self,param,column_name):

        sql = "UPDATE sub_actv_song_mood_stats SET "+column_name+" = %s WHERE subject = %s AND activity = %s"
        return self.db_connection.update_data(sql,param)

    def update_stats_submood_songmood(self, param, column_name):
        sql = "UPDATE stats_submood_songmood SET "+column_name+" = %s WHERE subject = %s AND submood = %s"
        return self.db_connection.update_data(sql,param)

    def update_stats_submood_genretype(self,param, column_name):
        sql = "UPDATE stats_submood_genretype SET "+column_name+" =%s WHERE subject = %s AND submood = %s"
        return self.db_connection.update_data(sql,param)

    def update_sub_mood_stats(self,param):
        sql = "REPLACE into sub_mood_stats VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self.db_connection.update_data(sql, param)

    def update_p_value(self,param):
        sql = "INSERT INTO score VALUES(%s,%s,%s,%s,%s)"
        return self.db_connection.update_data(sql,param)

    def initial_type_stats(self):
        sql = "insert into sub_mood_type()" \
            "VALUES()"
        return self.db_connection.update_data(sql,[])

    def initial_song_mood(self):
        sql = "insert into sub_mood_stats()" \
            "VALUES()"
        return self.db_connection.update_data(sql,[])

    def initial_act_genre_stats(self, param):
        sql = "INSERT INTO sub_actv_genre_stats(subject,activity, empty,blues,classical,country,easylistening,electronic,folk," \
            "holiday,international,jazz,latin,newage,poprock,rb,stagescreen) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        return self.db_connection.update_data(sql,param)

    def initial_stats_submood_songmood(self,param):
        sql = "INSERT INTO stats_submood_songmood(subject,submood,angry,blessed,complex,excited,happy,melancholic,peaceful,restless,sad,scared) "\
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self.db_connection.update_data(sql,param)

    def initial_stats_submood_genretype(self,param):
        sql = "INSERT INTO stats_submood_genretype(subject,submood, empty,blues,classical,country,easylistening,electronic,folk," \
            "holiday,international,jazz,latin,newage,poprock,rb,stagescreen) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self.db_connection.update_data(sql,param)

    def initial_act_song_mood_stats(self,param):
        sql = "INSERT INTO sub_actv_song_mood_stats(subject,activity,angry,blessed,complex,excited,happy,melancholic,peaceful,restless,sad,scared)" \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        return self.db_connection.update_data(sql,param)


    def get_user_type_stats(self,id):
        param = [str(id)]
        sql = "select * from sub_type_stats where subject = %s"
        return self.db_connection.fetch_data(sql, param)

    def get_user_song_mood_stats(self,id):
        param = [str(id)]
        sql = "select * from sub_song_mood where subject = %s"
        return self.db_connection.fetch_data(sql,param)

    def get_actv_genre(self,id):
        param = [str(id)]
        sql = "select * from sub_actv_genre where subject = %s"
        return self.db_connection.fetch_data(sql, param)

    def get_acty_song_mood(self,id):
        param = [str(id)]
        sql = "select * from sub_activity_song_mood where subject = %s"
        return self.db_connection.fetch_data(sql,param)

    def get_submood_songmood(self,id):
        param = [str(id)]
        sql = "select * from raw_mood_songmood where subject = %s"
        return self.db_connection.fetch_data(sql,param)

    def get_submood_genretype(self,id):
        param = [str(id)]
        sql = "select * from raw_submood_genretype where subject = %s"
        return self.db_connection.fetch_data(sql,param)

    def get_act_type(self,id):
        param = [str(id)]
        sql = "select DISTINCT (activity) AS type from sub_actv_genre where subject = %s"
        return self.db_connection.fetch_data(sql, param)

    def get_submood_type(self,id):
        param = [str(id)]
        sql = "select DISTINCT (mood) AS submoodtype from raw_mood_songmood where subject = %s"
        return self.db_connection.fetch_data(sql, param)

    def get_stats_data(self,table,id):
        param = [str(id)]
        if table == "submood_genretype":
            sql = "select blues,classical,country,easylistening,electronic,folk,holiday,international,jazz,latin,newage,poprock,rb,stagescreen FROM stats_submood_genretype" \
                  " WHERE subject = %s "
            return self.db_connection.fetch_data(sql, param)
        elif table =="submood_songmood":
            sql = "select angry,blessed,complex,excited,happy,melancholic,peaceful,restless,sad,scared FROM stats_submood_songmood" \
                  " WHERE subject = %s "
            return self.db_connection.fetch_data(sql,param)

        elif table =="actv_genretype":
            sql = "select blues,classical,country,easylistening,electronic,folk,holiday,international,jazz,latin,newage,poprock,rb,stagescreen FROM sub_actv_genre_stats" \
                  " WHERE subject = %s "
            return self.db_connection.fetch_data(sql,param)
        else:
            sql = "select angry,blessed,complex,excited,happy,melancholic,peaceful,restless,sad,scared FROM sub_actv_song_mood_stats" \
                  " WHERE subject = %s "
            return self.db_connection.fetch_data(sql, param)