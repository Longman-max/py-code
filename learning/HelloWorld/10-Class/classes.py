class Students:
    #  a attribute for data from
    def __init__(
            self,
            status,
            academic_year,
            student_id,
            first_name,
            middle_name,
            last_name,
            nationality,
            LGA,
            relation,
            relation_name
    ):
        # constructors help to fetch data from the user
        self.status = status
        self.year = academic_year
        self.id = student_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.lastname = last_name
        self.nationality = nationality
        self.lga = LGA
        self.relation = relation
        self.relation_name = relation_name

        
class Teacher:
    def __init__(
            self,
            status,
            title,
            first_name,
            middle_name,
            last_name,
            phone,
            marital_status,
            nationality,
            session,
            gender
    ):
        self.status = status
        self.title = title
        self.first_name = first_name
        self.middle_name = middle_name
        self.lastname = last_name
        self.contact = phone
        self.marital = marital_status
        self.nationality = nationality
        self.session = session
        self.gender = gender
