



previousQuestion = () => {
    history.back() ;
}

nextQuestion = id => {
    id ++ ;
    location.href = `${id}` ;
}