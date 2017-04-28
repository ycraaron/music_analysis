from scipy.stats import chi2_contingency
from scipy.stats import chisquare
import numpy as np

import mdl_data

GENRETYPE = 14
SUBMOOD = 10

class Core:
    def __init__(self):
        self.data_instance = mdl_data.MdlData()

        if self.data_instance.is_connected():
            print(self.data_instance.is_connected())
        else:
            print("Fail to connect to DB")
            quit(0)

    def initial_type(self):
        for i in range(0, 48):
            print i
            self.data_instance.initial_type_stats()

    def initial_song_mood(self):
        for i in range(0,48):
            print i
            self.data_instance.initial_song_mood()

    def update_submood(self):
        for i in range(0,48):
            result = self.data_instance.get_user_type_stats(i)
            ls = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]

            for item in result:
                type = item["genre_type"]
                subject = item["subject"]
                count = item["count"]
                type = str(type)

                print type,subject,count
                ls[0] = str(int(subject) + 1)
                if type == "0":
                    ls[1]=str(count)
                elif type == "Blues":
                    ls[2]=str(count)
                elif type == "Classical":
                    ls[3]=str(count)
                elif type == "Country":
                    ls[4]=str(count)
                elif type == "Easy Listening":
                    ls[5]=str(count)
                elif type == "Electronic":
                    ls[6]=str(count)
                elif type == "Folk":
                    ls[7]=str(count)
                elif type == "Holiday":
                    ls[8]=str(count)
                elif type == "International":
                    ls[9]=str(count)
                elif type == "Jazz":
                    ls[10]=str(count)
                elif type == "Latin":
                    ls[11]=str(count)
                elif type == "New Age":
                    ls[12]=str(count)
                elif type == "Pop/Rock":
                    ls[13]=str(count)
                elif type == "R&B(Rhythm and Blues)":
                    ls[14]=str(count)
                elif type == "Stage & Screen":
                    ls[15]=str(count)
                else:
                    print "error"
            print self.data_instance.update_music_type(ls)





            #self.update_sub_music_type(result)

    #def update_sub_music_type(self):

    def initial_act_genre(self):
        for i in range(0, 48):
            result_type = self.data_instance.get_act_type(i)

            #print result_type
            #print result_data

            for type in result_type:
                ls = [str(i), type["type"], "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
                print self.data_instance.initial_act_genre_stats(ls)

    def initial_act_song_mood(self):
        for i in range(0, 48):
            result_type = self.data_instance.get_act_type(i)

            for type in result_type:
                ls = [str(i), type["type"], "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
                print self.data_instance.initial_act_song_mood_stats(ls)

    def initial_stats_submood_songmood(self):
        for i in range(0,48):
            result_type = self.data_instance.get_submood_type(i)

            for type in result_type:
                ls = [str(i), type["submoodtype"], "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
                print self.data_instance.initial_stats_submood_songmood(ls)

    def initial_stats_submood_genretype(self):
        for i in range(0,48):
            result_type = self.data_instance.get_submood_type(i)

            for type in result_type:
                ls = [str(i), type["submoodtype"],"0", "0", "0", "0", "0","0", "0", "0", "0", "0","0", "0", "0", "0", "0"]
                print self.data_instance.initial_stats_submood_genretype(ls)

    def update_act_genre(self):
        for i in range(0,48):
            result_data = self.data_instance.get_actv_genre(i)
            print result_data

            for item in result_data:
                activity = item["activity"]
                subject  = item["subject"]
                type     = item["genre_type"]
                count    = item["count"]
                #[column_name, count, subject, activity]
                ls = [str(count), str(subject), str(activity)]

                # if type == "0":
                #     ls[0] = "empty"
                # elif type == "Blues":
                #     ls[0] = "blues"
                # elif type == "Classical":
                #     ls[0] = "classical"
                # elif type == "Country":
                #     ls[0] = "country"
                # elif type == "Easy Listening":
                #     ls[0] = "easylistening"
                # elif type == "Electronic":
                #     ls[0] = "electronic"
                # elif type == "Folk":
                #     ls[0] = "folk"
                # elif type == "Holiday":
                #     ls[0] = "holiday"
                # elif type == "International":
                #     ls[0] = "international"
                # elif type == "Jazz":
                #     ls[0] = "jazz"
                # elif type == "Latin":
                #     ls[0] = "latin"
                # elif type == "New Age":
                #     ls[0] = "newage"
                # elif type == "Pop/Rock":
                #     ls[0] = "poprock"
                # elif type == "R&B(Rhythm and Blues)":
                #     ls[0] = "rb"
                # elif type == "Stage & Screen":
                #     ls[0] = "stagescreen"
                # else:
                #     print "error"

                if type == "0":
                    type = "empty"
                elif type == "Blues":
                    type = "blues"
                elif type == "Classical":
                    type = "classical"
                elif type == "Country":
                    type = "country"
                elif type == "Easy Listening":
                    type = "easylistening"
                elif type == "Electronic":
                    type = "electronic"
                elif type == "Folk":
                    type = "folk"
                elif type == "Holiday":
                    type = "holiday"
                elif type == "International":
                    type = "international"
                elif type == "Jazz":
                    type = "jazz"
                elif type == "Latin":
                    type = "latin"
                elif type == "New Age":
                    type = "newage"
                elif type == "Pop/Rock":
                    type = "poprock"
                elif type == "R&B(Rhythm and Blues)":
                    type = "rb"
                elif type == "Stage & Screen":
                    type = "stagescreen"
                else:
                    print "error"

                print self.data_instance.update_act_stats(ls, type)

    def update_act_song_mood_stats(self):
        for i in range(0, 48):
            result_data = self.data_instance.get_acty_song_mood(i)
            print result_data

            for item in result_data:
                activity = item["activity"]
                subject  = item["subject"]
                type     = item["mood"]
                count    = item["count"]
                #[column_name, count, subject, activity]
                ls = [str(count), str(subject), str(activity)]


                print self.data_instance.update_act_song_mood_stats(ls, type)

    def update_stats_submood_songmood(self):
        for i in range(0, 48):
            result_data = self.data_instance.get_submood_songmood(i)
            print result_data

            for item in result_data:
                submood = item["mood"]
                songmood = item["songmood"]
                subject = item["subject"]
                count = item["count"]

                ls = [str(count),str(subject),str(submood)]
                print self.data_instance.update_stats_submood_songmood(ls,songmood)

    def update_stats_submood_genretype(self):
        for i in range(0,48):
            result_data = self.data_instance.get_submood_genretype(i)

            for item in result_data:
                print result_data
                count = item["count"]
                subject = item["subject"]
                submood = item["mood"]
                type = item["genretype"]

                ls = [str(count),str(subject),str(submood)]

                if type == "0":
                    type = "empty"
                elif type == "Blues":
                    type = "blues"
                elif type == "Classical":
                    type = "classical"
                elif type == "Country":
                    type = "country"
                elif type == "Easy Listening":
                    type = "easylistening"
                elif type == "Electronic":
                    type = "electronic"
                elif type == "Folk":
                    type = "folk"
                elif type == "Holiday":
                    type = "holiday"
                elif type == "International":
                    type = "international"
                elif type == "Jazz":
                    type = "jazz"
                elif type == "Latin":
                    type = "latin"
                elif type == "New Age":
                    type = "newage"
                elif type == "Pop/Rock":
                    type = "poprock"
                elif type == "R&B(Rhythm and Blues)":
                    type = "rb"
                elif type == "Stage & Screen":
                    type = "stagescreen"
                else:
                    print "error"

                print self.data_instance.update_stats_submood_genretype(ls,type)

    def update_user_song_mood_stats(self):
        for i in range(0,48):
            result = self.data_instance.get_user_song_mood_stats(i)
            ls = ["0","0","0","0","0","0","0","0","0","0","0"]

            for item in result:
                count = item["count"]
                type = item["mood"]
                subject = item["subject"]

                ls[0] = str(int(subject) + 1)
                if type == "angry":
                    ls[1]=str(count)
                elif type == "blessed":
                    ls[2]=str(count)
                elif type == "complex":
                    ls[3]=str(count)
                elif type == "excited":
                    ls[4]=str(count)
                elif type == "happy":
                    ls[5]=str(count)
                elif type == "melancholic":
                    ls[6]=str(count)
                elif type == "peaceful":
                    ls[7]=str(count)
                elif type == "restless":
                    ls[8]=str(count)
                elif type == "sad":
                    ls[9]=str(count)
                elif type == "scared":
                    ls[10]=str(count)
                else:
                    print "error"

                print self.data_instance.update_sub_mood_stats(ls)

            print result

    def remove_zero(self, obs, lengthy, lengthx):

        np.array(zip(*(i for i in zip(*obs) if i.count(0) < len(i) / 2)))

        #obs[:, (obs != 0).sum(axis=0) >= 5]
        #print obs
        ls_remove_tag = []
        print obs
        for i in range(0,lengthx):
            count = 0
            for j in range(0,lengthy):
                count += obs[j][i]
            if count == 0:
                ls_remove_tag.append(i)

        print ls_remove_tag

        deleted_obs = np.delete(obs, ls_remove_tag, axis=1)

        print deleted_obs

        return deleted_obs

    def cal_p_value(self,result,tag):
        count = len(result)
        #print result
        ls_obs = []
        for item in result:
            if tag == "submood_genretype" or tag == "actv_genretype":
                ls = [item['blues'], item['classical'], item['country'], item['easylistening'], item['electronic'],
                      item['folk'], item['holiday'], item['international'], item['jazz'], item['latin'], item['newage'],
                      item['poprock'], item['rb'], item['stagescreen']]
                ls_obs.append(ls)
            else:
                ls = [item['angry'],item['blessed'],item['complex'],item['excited'],item['happy'],item['melancholic'],
                      item['peaceful'],item['restless'],item['sad'],item['scared']]
                ls_obs.append(ls)

        obs = np.array(ls_obs, ndmin=2)
        if tag == "submood_genretype" or tag == "actv_genretype":
            deleted_obs = self.remove_zero(obs, count, GENRETYPE)
        else:
            deleted_obs = self.remove_zero(obs, count, SUBMOOD)
        chi2, p, dof, ex = chi2_contingency(deleted_obs, correction=False)
        return p

    def cal(self):
        for i in range(0,48):

            result_submood_genretype = self.data_instance.get_stats_data("submood_genretype",i)
            result_submood_songmood  = self.data_instance.get_stats_data("submood_songmood",i)
            result_actv_genretype    = self.data_instance.get_stats_data("actv_genretype",i)
            result_actv_songmood     = self.data_instance.get_stats_data("actv_songmood",i)

            p1 = self.cal_p_value(result_submood_genretype,"submood_genretype")
            p2 = self.cal_p_value(result_submood_songmood,"submood_songmood")
            p3 = self.cal_p_value(result_actv_genretype,"actv_genretype")
            p4 = self.cal_p_value(result_actv_songmood,"actv_songmood")

            param = [str(i),str(p1),str(p2),str(p3),str(p4)]

            self.data_instance.update_p_value(param)








entry = Core()

#entry.initial_act_song_mood()
#entry.initial_song_mood()

#entry.update_user_song_mood_stats()

#entry.update_submood()

#entry.initial_act_genre()

#entry.update_act_genre()

#entry.update_act_song_mood_stats()

#entry.initial_stats_submood_songmood()

#entry.update_stats_submood_songmood()

#entry.initial_stats_submood_genretype()

#entry.update_stats_submood_genretype()

entry.cal()


