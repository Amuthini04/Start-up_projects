#include <stdio.h>

int main() {
    float members[4][2]; // 2D array to store height and weight of 4 members
    float bmi[4]; // array to store BMI of 4 members

    // input height and weight of 4 members
    for (int i = 0; i < 4; i++) {
        printf("Enter height and weight of member %d (in meters and kilograms): ", i+1);
        scanf("%f %f", &members[i][0], &members[i][1]);
    }

    // calculate BMI of 4 members
    for (int i = 0; i < 4; i++) {
        bmi[i] = members[i][1] / (members[i][0] * members[i][0]);
    }

    // print BMI of 4 members
    printf("\nBMI of 4 members:\n");
    for (int i = 0; i < 4; i++) {
        printf("Member %d: %.2f\n", i+1, bmi[i]);
    }

    return 0;
}
