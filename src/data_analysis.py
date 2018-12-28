import matplotlib.pyplot as plt
import matplotlib
import collections
import numpy as np

def audience_analysis(entries):

    # Draw histogram of professors' ages
    ages = [e.professor.age for e in entries if e.professor.age]
    plt.hist(ages, bins=range(20, 75, 5), facecolor='lightblue')
    plt.ylabel('Frequency')
    plt.xlabel('Ages')
    plt.title('Histogram of ages')
    plt.savefig('img/age_histogram.png')
    plt.close()

    # Draw histogram of professors' experiences
    years_experience = [e.professor.yearsexp for e in entries if e.professor.yearsexp]
    plt.hist(years_experience, bins=range(0, 45, 5), facecolor='lightblue')
    plt.ylabel('Frequency')
    plt.xlabel('Years of experience')
    plt.title('Histogram of years of experience')
    plt.savefig('img/experience_histogram.png')
    plt.close()


    # By gender
    gender_counter = collections.Counter([e.professor.gender for e in entries])
    men = gender_counter[0]
    women = gender_counter[1]
    gender_quantities = [men, women]
    gender_labels = ['Men', 'Women']
    gender_colors = ['#79d279', 'lightblue']
    gender_explode = [0, 0.1]
    fig_gender, ax_gender = plt.subplots()
    ax_gender.pie(gender_quantities, explode=gender_explode, labels=gender_labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=gender_colors)
    ax_gender.axis('equal')
    plt.savefig('img/gender.png')
    plt.close()


    # By level
    level_counter = collections.Counter([e.professor.phd for e in entries])
    phd_yes = level_counter[1]
    phd_no = level_counter[0]
    level_labels = ['With PHD', 'No PHD']
    level_y = range(0, len(level_labels))
    level_quantities = [phd_yes, phd_no]
    plt.barh(level_y, level_quantities, align='center', alpha=0.5)
    plt.yticks(level_y, level_labels)
    plt.xlabel('Quantity')
    plt.title('By level')
    plt.savefig('img/level.png')
    plt.close()


    # By wiki registration
    user_wiki_counter = collections.Counter([e.professor.userwiki for e in entries])
    user_wiki_yes = user_wiki_counter[1]
    user_wiki_no = user_wiki_counter[0]
    registration_labels = ['Yes', 'No']
    registration_y = range(0, len(registration_labels))
    registration_quantities = [user_wiki_yes, user_wiki_no]
    plt.barh(registration_y, registration_quantities, align='center', alpha=0.5)
    plt.yticks(registration_y, registration_labels)
    plt.xlabel('Quantity')
    plt.title('By registration on Wikipedia')
    plt.savefig('img/wikipedia.png')
    plt.close()


    # By university
    university_counter = collections.Counter([e.professor.university for e in entries])
    university_uoc = university_counter[1]
    university_upf = university_counter[2]
    university_labels = ['UOC', 'UPF']
    university_y = range(0, len(university_labels))
    university_quantities = [university_uoc, university_upf]
    plt.barh(university_y, university_quantities, align='center', alpha=0.5)
    plt.yticks(university_y, university_labels)
    plt.xlabel('Quantity')
    plt.title('By University')
    plt.savefig('img/university.png')
    plt.close()


    # By domain (pie)
    domain_counter = collections.Counter([e.professor.domain for e in entries])
    arts = domain_counter[1]
    sciences = domain_counter[2]
    health_sciences = domain_counter[3]
    engineering = domain_counter[4]
    law = domain_counter[5]
    domain_labels = ['Arts & Humanities', 'Engineering & Architecture', 'Health Sciences', 'Sciences', 'Law & Politics.']
    domain_quantities = [arts, engineering, health_sciences, sciences, law]
    domain_explode = [0.1] * len(domain_labels)
    fig_domain, ax_domain = plt.subplots()
    ax_domain.pie(domain_quantities, explode=domain_explode, labels=domain_labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax_domain.axis('equal')
    plt.savefig('img/domain.png')
    plt.close()

def enjoyment_analysis(entries):

    # Analysis of the parameters ENJ1 and ENJ2.
    # Here we consider that a person:
    # - disagrees with a statement if they answer 1 or 2.
    # - is neutral regarding a statement if they answer 3.
    # - agrees with a statement if they answer 4 or 5.

    meanAge = np.mean([e.professor.age for e in entries if e.professor.age])
    meanAgeAgreeEnj1 = np.mean([e.professor.age for e in entries if e.enjoyment.enj1 >= 4])
    meanAgeDisagreeEnj1 = np.mean([e.professor.age for e in entries if e.enjoyment.enj1 <= 2])
    medianAgeAgreeEnj1 = np.median([e.professor.age for e in entries if e.enjoyment.enj1 >= 4])
    medianAgeDisagreeEnj1 = np.median([e.professor.age for e in entries if e.enjoyment.enj1 <= 2])

    print 'Mean age among all professors: ' + str(meanAge)
    print 'Mean age among professors that agree (ENJ1): ' + str(meanAgeAgreeEnj1)
    print 'Mean age among professors that disagree (ENJ1): ' + str(meanAgeDisagreeEnj1)
    print 'Median age among professors that agree (ENJ1): ' + str(medianAgeAgreeEnj1)
    print 'Median age among professors that disagree (ENJ1): ' + str(medianAgeDisagreeEnj1)

    meanAge = np.mean([e.professor.age for e in entries if e.professor.age])
    meanAgeAgreeEnj2 = np.mean([e.professor.age for e in entries if e.enjoyment.enj2 >= 4])
    meanAgeDisagreeEnj2 = np.mean([e.professor.age for e in entries if e.enjoyment.enj2 <= 2])
    medianAgeAgreeEnj2 = np.median([e.professor.age for e in entries if e.enjoyment.enj2 >= 4])
    medianAgeDisagreeEnj2 = np.median([e.professor.age for e in entries if e.enjoyment.enj2 <= 2])

    print 'Mean age among professors that agree (ENJ2): ' + str(meanAgeAgreeEnj2)
    print 'Mean age among professors that disagree (ENJ2): ' + str(meanAgeDisagreeEnj2)
    print 'Median age among professors that agree (ENJ2): ' + str(medianAgeAgreeEnj2)
    print 'Median age among professors that disagree (ENJ2): ' + str(medianAgeDisagreeEnj2)

    
    meanENJ1 = np.mean([e.enjoyment.enj1 for e in entries if e.enjoyment.enj1])
    meanENJ1RegisteredProfessors = np.mean([e.enjoyment.enj1 for e in entries if e.enjoyment.enj1 and e.professor.userwiki == 1])
    meanENJ1NonRegisteredProfessors = np.mean([e.enjoyment.enj1 for e in entries if e.enjoyment.enj1 and e.professor.userwiki == 0])
    print '-------'
    print 'Mean rate among all professors (ENJ1): ' + str(meanENJ1)
    print 'Mean rate among registered professors on Wikipedia (ENJ1): ' + str(meanENJ1RegisteredProfessors)
    print 'Mean rate among non-registered professors on Wikipedia (ENJ1): ' + str(meanENJ1NonRegisteredProfessors)

    meanENJ2 = np.mean([e.enjoyment.enj2 for e in entries if e.enjoyment.enj2])
    meanENJ2RegisteredProfessors = np.mean([e.enjoyment.enj2 for e in entries if e.enjoyment.enj2 and e.professor.userwiki == 1])
    meanENJ2NonRegisteredProfessors = np.mean([e.enjoyment.enj2 for e in entries if e.enjoyment.enj2 and e.professor.userwiki == 0])
    print 'Mean rate among all professors (ENJ2): ' + str(meanENJ2)
    print 'Mean rate among registered professors on Wikipedia (ENJ2): ' + str(meanENJ2RegisteredProfessors)
    print 'Mean rate among non-registered professors on Wikipedia (ENJ2): ' + str(meanENJ2NonRegisteredProfessors)


    # Analysis of ENJ1 and ENJ2 per professors divided by domain. For each domain we verify the mean of the answers given by the professors
    # that belong to it.
    
    meanPerDomainEnj1 = {d : (np.mean([e.enjoyment.enj1 for e in entries if e.enjoyment.enj1 and e.professor.domain == d])) for d in range(1,6)}
    meanArtsEnj1 = meanPerDomainEnj1[1]
    meanSciencesEnj1 = meanPerDomainEnj1[2]
    meanHealthScienceEnj1 = meanPerDomainEnj1[3]
    meanEngineeringEnj1 = meanPerDomainEnj1[4]
    meanLawEnj1 = meanPerDomainEnj1[5]
    print '-------'
    print 'Mean by domain (ENJ1):'
    print 'Mean Arts (ENJ1): ' + str(meanArtsEnj1)
    print 'Mean Sciences (ENJ1): ' + str(meanSciencesEnj1)
    print 'Mean Health Sciences (ENJ1): ' + str(meanHealthScienceEnj1)
    print 'Mean Engineering (ENJ1): ' + str(meanEngineeringEnj1)
    print 'Mean Law (ENJ1): ' + str(meanLawEnj1)

    meanPerDomainEnj2 = {d : (np.mean([e.enjoyment.enj2 for e in entries if e.enjoyment.enj2 and e.professor.domain == d])) for d in range(1,6)}
    meanArtsEnj2 = meanPerDomainEnj2[1]
    meanSciencesEnj2 = meanPerDomainEnj2[2]
    meanHealthScienceEnj2 = meanPerDomainEnj2[3]
    meanEngineeringEnj2 = meanPerDomainEnj2[4]
    meanLawEnj2 = meanPerDomainEnj2[5]
    print 'Mean by domain (ENJ2):'
    print 'Mean Arts (ENJ2): ' + str(meanArtsEnj2)
    print 'Mean Sciences (ENJ2): ' + str(meanSciencesEnj2)
    print 'Mean Health Sciences (ENJ2): ' + str(meanHealthScienceEnj2)
    print 'Mean Engineering (ENJ2): ' + str(meanEngineeringEnj2)
    print 'Mean Law (ENJ2): ' + str(meanLawEnj2)


def other_analysis(entries):

    # Analysis of QU4, which considers the lack of quality of Wikipedia content in the area of expertise of the professor (the bigger, the worse)
    meanPerDomainQU4 = {d : (np.mean([e.quality.qu4 for e in entries if e.quality.qu4 and e.professor.domain == d])) for d in range(1,6)}
    meanArtsQu4 = meanPerDomainQU4[1]
    meanSciencesQu4 = meanPerDomainQU4[2]
    meanHealthScienceQu4 = meanPerDomainQU4[3]
    meanEngineeringQu4 = meanPerDomainQU4[4]
    meanLawQu4 = meanPerDomainQU4[5]
    print '-------'
    print 'Mean by domain (QU4):'
    print 'Mean Arts (QU4): ' + str(meanArtsQu4)
    print 'Mean Sciences (QU4): ' + str(meanSciencesQu4)
    print 'Mean Health Sciences (QU4): ' + str(meanHealthScienceQu4)
    print 'Mean Engineering (QU4): ' + str(meanEngineeringQu4)
    print 'Mean Law (QU4): ' + str(meanLawQu4)


    # Experience (per age and domain)
    ageIntervals = range(0, 10)
    means_experience = np.zeros((len(ageIntervals), 5))
    for d in range(1,6):
        for ix in ageIntervals:
            interval = range(20 + ix * 5, 25 + ix * 5)
            mean = np.mean([np.mean([e.experience.exp1, e.experience.exp2, e.experience.exp3, e.experience.exp4, e.experience.exp5])
                for e in entries if e.experience.exp1 and e.experience.exp2 and e.experience.exp3 and e.experience.exp4 and e.experience.exp5 and
                e.professor.domain == d and e.professor.age in interval])
            means_experience[ix][d - 1] = round(mean, 2)

    ages_labels = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-70']
    domains_labels = ['Arts & Humanities', 'Sciences', 'Health Sciences', 'Engineering & Architecture', 'Law & Politics.']

    fig_experience, ax_experience = plt.subplots()
    im = ax_experience.imshow(means_experience, cmap='OrRd')
    ax_experience.set_xticks(np.arange(len(domains_labels)))
    ax_experience.set_yticks(np.arange(len(ages_labels)))
    ax_experience.set_xticklabels(domains_labels)
    ax_experience.set_yticklabels(ages_labels)
    plt.setp(ax_experience.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
    for i in range(len(ages_labels)):
        for j in range(len(domains_labels)):
            text = ax_experience.text(j, i, means_experience[i, j], ha='center', va='center', color='k')
    ax_experience.set_title('Mean of Experience categories (per domain, per age interval)')
    fig_experience.tight_layout()
    plt.savefig('img/heatmap.png')
    plt.close()