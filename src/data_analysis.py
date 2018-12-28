import matplotlib.pyplot as plt
import matplotlib
import collections

def audience_analysis(entries):

    # Draw histogram of professors' ages
    ages = [e.professor.age for e in entries if e.professor.age]
    plt.hist(ages, bins=range(20, 75, 5), facecolor='lightblue')
    plt.ylabel("Frequency")
    plt.xlabel("Ages")
    plt.title("Histogram of ages")
    plt.savefig("img/age_histogram.png")
    plt.close()

    # Draw histogram of professors' experiences
    years_experience = [e.professor.yearsexp for e in entries if e.professor.yearsexp]
    plt.hist(years_experience, bins=range(0, 45, 5), facecolor='lightblue')
    plt.ylabel("Frequency")
    plt.xlabel("Years of experience")
    plt.title("Histogram of years of experience")
    plt.savefig("img/experience_histogram.png")
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
    plt.savefig("img/domain.png")
    plt.close()