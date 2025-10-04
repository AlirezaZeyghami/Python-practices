class School:
    def __init__(self, student_count):
        self.student_count = student_count
        self.ages = []
        self.heights = []
        self.weights = []

    def set_ages(self, ages):
        self.ages = ages

    def set_heights(self, heights):
        self.heights = heights

    def set_weights(self, weights):
        self.weights = weights

    def age_avg(self):
        return float(sum(self.ages) / self.student_count)

    def height_avg(self):
        return float(sum(self.heights) / self.student_count)

    def weight_avg(self):
        return float(sum(self.weights) / self.student_count)


def make_school():
    count = int(input())
    ages = list(map(float, input().split()))
    heights = list(map(float, input().split()))
    weights = list(map(float, input().split()))
    school = School(count)
    school.set_ages(ages)
    school.set_heights(heights)
    school.set_weights(weights)
    return school


# Milk is distributed.
school_a = make_school()
# Milk is not distributed.
school_b = make_school()

a_age_avg = school_a.age_avg()
print(a_age_avg)
a_height_avg = school_a.height_avg()
print(a_height_avg)
a_weight_avg = school_a.weight_avg()
print(a_weight_avg)

b_age_avg = school_b.age_avg()
print(b_age_avg)
b_height_avg = school_b.height_avg()
print(b_height_avg)
b_weight_avg = school_b.weight_avg()
print(b_weight_avg)

a_height = school_a.height_avg()
b_height = school_b.height_avg()
a_weight = school_a.weight_avg()
b_weight = school_b.weight_avg()


if a_height > b_height:
    print("A")
elif a_height < b_height:
    print("B")
elif a_weight < b_weight:
    print("A")
elif a_weight > b_weight:
    print("B")
else:
    print("Same")
