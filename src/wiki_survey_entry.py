import collections

Professor = collections.namedtuple(
    'professor',
    'age,'
    # 0=Male; 1=Female.
    'gender,'
    # 1=Arts & Humanities; 2=Sciences; 3=Health Sciences; 4=Engineering & Architecture; 5=Law & Politics.
    'domain,'
    # 0=No; 1=Yes.
    'phd,'
    # Years of university teaching experience.
    'yearsexp,'
    # 1=UOC; 2=UPF.
    'university,'
    # Academic position of UOC members: 1=Professor; 2=Associate; 3=Assistant; 4=Lecturer; 5=Instructor; 6=Adjunct .
    'uoc_position,'
    # Work as part-time in another university and UPF members:
    # 1=Professor; 2=Associate; 3=Assistant; 4=Lecturer; 5=Instructor; 6=Adjunct.
    'other_position,'
    # Main job in another university for part-time members: 1=Yes; 2=No
    'otherstatus,'
    # Wikipedia registered user: 0=No; 1=Yes
    'userwiki,'
)


Usefulness = collections.namedtuple(
    'usefulness',
    'pu1,'  # The use of Wikipedia makes it easier for students to develop new skills.
    'pu2,'  # The use of Wikipedia improves students' learning.
    'pu3,'  # Wikipedia is useful for teaching.
)

EaseOfUse = collections.namedtuple(
    'ease_of_use',
    'peu1,'  # Wikipedia is user-friendly.
    'peu2,'  # It is easy to find in Wikipedia the information you seek.
    'peu3,'  # It is easy to add or edit information in Wikipedia.
)

Enjoyment = collections.namedtuple(
    'enjoyment',
    'enj1,'  # The use of Wikipedia stimulates curiosity.
    'enj2,'  # The use of Wikipedia is entertaining.
)


Quality = collections.namedtuple(
    'quality',
    'qu1,'  # Articles in Wikipedia are reliable.
    'qu2,'  # Articles in Wikipedia are updated.
    'qu3,'  # Articles in Wikipedia are comprehensive.
    'qu4,'  # In my area of expertise, Wikipedia has a lower quality than other educational resources.
    'qu5,'  # I trust in the editing system of Wikipedia.
)


Visibility = collections.namedtuple(
    'visibility',
    'vis1,'  # Wikipedia improves visibility of students' work.
    'vis2,'  # It is easy to have a record of the contributions made in Wikipedia.
    'vis3,'  # I cite Wikipedia in my academic papers.
)


SocialImage = collections.namedtuple(
    'social_image',
    'im1,'  # The use of Wikipedia is well considered among colleagues.
    'im2,'  # In academia, sharing open educational resources is appreciated.
    'im3,'  # My colleagues use Wikipedia.
)


SharingAttitude = collections.namedtuple(
    'sharing_attitude',
    'sa1,'  # It is important to share academic content in open platforms.
    'sa2,'  # It is important to publish research results in other media than academic journals or books.
    'sa3,'  # It is important that students become familiar with online collaborative environments.
)


UseBehaviour = collections.namedtuple(
    'use_behaviour',
    'use1,'  # I use Wikipedia to develop my teaching materials.
    'use2,'  # I use Wikipedia as a platform to develop educational activities with students.
    'use3,'  # I recommend my students to use Wikipedia.
    'use4,'  # I recommend my colleagues to use Wikipedia.
    'use5,'  # I agree my students use Wikipedia in my courses.
)


Profile = collections.namedtuple(
    'profile',
    'pf1,'  # I contribute to blogs.
    'pf2,'  # I actively participate in social networks.
    'pf3,'  # I publish academic content in open platforms.
)


JobRelevance = collections.namedtuple(
    'job_relevance',
    'jr1,'  # My university promotes the use of open collaborative environments in the Internet.
    'jr2,'  # My university considers the use of open collaborative environments in the Internet as a teaching merit.
)


BehavioralIntention = collections.namedtuple(
    'behavioral_intention',
    'bi1,'  # In the future I will recommend the use of Wikipedia to my colleagues and students.
    'bi2,'  # In the future I will use Wikipedia in my teaching activity.
)


Incentives = collections.namedtuple(
    'incentives',
    'inc1,'  # To design educational activities using Wikipedia, it would be helpful: a best practices guide.
    'inc2,'  # To design educational activities using Wikipedia, it would be helpful: getting instruction from a colleague.
    'inc3,'  # To design educational activities using Wikipedia, it would be helpful: getting specific training.
    'inc4,'  # To design educational activities using Wikipedia, it would be helpfull: greater institutional recognition.
)


Experience = collections.namedtuple(
    'experience',
    'exp1,'  # I consult Wikipedia for issues related to my field of expertise.
    'exp2,'  # I consult Wikipedia for other academic related issues.
    'exp3,'  # I consult Wikipedia for personal issues.
    'exp4,'  # I contribute to Wikipedia (editions, revisions, articles improvement...).
    'exp5,'  # I use wikis to work with my students.
)

# professor, perceived_usefulness, perceived_ease_of_use, perceived_enjoyment, quality, visibility, social_image, sharing_attitude, user_behaviour, profile2, job_relevance, behavioral_intention, incentives, experience
class WikiSurveyEntry:
    def __init__(self, **kwargs):

        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        # self.update
        # self.professor = professor
        # self.perceived_usefulness = kwargs('perceived_usefulness')
        # self.perceived_ease_of_use = kwargs('perceived_ease_of_use')
        # self.perceived_enjoyment = kwargs('perceived_enjoyment')
        # self.quality = quawlity
        # self.visibility = kwargs('visibility')
        # self.social_image = kwargs('social_image')
        # self.sharing_attitude = kwargs('sharing_attitude')
        # self.user_behaviour = kwargs('user_behaviour')
        # self.profile2 = kwargs('profile2')
        # self.job_relevance = kwargs('job_relevance')
        # self.behavioral_intention = kwargs('behavioral_intention')
        # self.incentives = kwargs('incentives')
        # self.experience = kwargs('experience')