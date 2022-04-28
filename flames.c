#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void RemoveSpace(char *name)
{
    int j=0;
    for(int i=0; i<strlen(name); i++)
    {
        if (name[i] != ' ')
            name[j++] = name[i];
    }
    name[j]='\0';
}

int main()
{
    int count,flcount;
    char person1[50],person2[50],countchar[50], p1[50],p2[50],fl[]="flames";
    printf("----kindly enter names in small letters---\n Let's play FLAMES relationship game.\n\nEnter First person Name: ");
    gets(person1);  // david

    printf("Enter partner person Name: ");
    gets(person2); // mercy
    strcpy(p1,person1);
    strcpy(p2,person2);
    RemoveSpace(person1);
    RemoveSpace(person2);
    // compare the both name and strike out commons
    for (int i=0; i<strlen(person1); ++i)
    {
        for (int j=0; j<strlen(person2); ++j)
        {
            if (person1[i] == person2[j])
            {
                person1[i]= ' ';
                person2[j]=' ';
                break;
            }
        }
    }
    // removing space and adding of charaters
    RemoveSpace(person1);
    RemoveSpace(person2);
    strcat(person1,person2);
    printf("\n\nCombination of both persons remaining letters '%s'.\n",person1);
    // flames game start here
    count = strlen(person1);
    if(count==0)
    {
        printf("After strike's not found of Characters.\n\n");
        exit(1);
    }
    printf("Balance letters Count is '%d'.\n",count);
    flcount = strlen(fl);
    for(int i=0; i<5;i++)
    {
        int rem , index=0;
        char cpybl[6] ,singlechar;
        rem = count%strlen(fl);
        printf("\n****Round %d strike in Flames***\n",i+1);
        if(rem == 0)
        {
            singlechar = fl[strlen(fl)-1];
            fl[strlen(fl)-1]=' ';
            RemoveSpace(fl);
        }
        else if(rem < strlen(fl) && rem != 1 && rem != 0)
        {
            singlechar = fl[rem-1];
            fl[rem-1]=' ';
            for(int j=0; j < strlen(fl); ++j)
            {
                if(j>=rem)
                {
                    cpybl[index++]= fl[j];
                    fl[j]=' ';
                }
            }
            strcat(cpybl,fl);
            RemoveSpace(cpybl);
            for(int k=0; k< strlen(cpybl); k++)
            {
              fl[k]=cpybl[k];
              cpybl[k]=' ';
            }
            RemoveSpace(cpybl);
            RemoveSpace(fl);
        }
        else if (rem ==1)
        {
            singlechar = fl[0];
            fl[0]=' ';
            RemoveSpace(fl);
        }
        printf("\nRemaining Characters are '%s' strikes letter is '%c' .\n ",fl,singlechar);

    }
    if(strlen(fl)==1)
    {
            printf("\n\n***************************************************************************\n\n");
            if( fl[0]=='f')
                printf("%s and %s are just a 'FRIENDS'.",p1,p2);
            if( fl[0]=='l')
                printf("%s and %s are in 'LOVING' relationship.",p1,p2);
            if( fl[0]=='a')
                printf("%s and %s both are 'AFFECTION' between each other.",p1,p2);
            if( fl[0]=='m')
                printf("%s and %s are guess they are 'MARRIAGE' in future or \n get marriage relationship.",p1,p2);
            if( fl[0]=='e')
                printf("%s and %s both are 'ENEMY' to each other",p1,p2);
            if( fl[0]=='s')
                printf("%s and %s both are just a brother and 'SISTER' relationship.",p1,p2);
    }
    printf("\n\n*************************************************************************** \n\n");






    return 0;
}
