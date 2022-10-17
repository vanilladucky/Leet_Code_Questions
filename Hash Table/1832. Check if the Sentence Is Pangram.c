bool checkIfPangram(char * sentence){
    int alpha[26] = {};
    int count = 0;
    while (*sentence != '\0'){
        int index = (int) *sentence++ - (int) 'a';
        if (alpha[index] != 1){
            alpha[index] = 1;
            count++;
        }
        else{
        }
    }
    if (count == 26){
        return true;
    }
    else{
        return false;
    }
}
