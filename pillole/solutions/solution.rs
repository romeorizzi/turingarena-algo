fn num_modi_ric(i: i64, h: i64) -> i64 {
    match (i, h) {
        (0, 0) => panic!("Imposible move"),
        (0, _) => 1,
        (i, 0) => num_modi_ric(i - 1, 1),
        (i, h) => num_modi_ric(i - 1, h + 1) + num_modi_ric(i, h - 1),
    }
}

pub fn num_modi(n: i64) -> i64 {
    return num_modi_ric(n, 0);
}

#[derive(Clone)]
enum Choice {
    TakeHalf, 
    TakeInteger,
}

fn elenca_modi_ric(i: i64, h: i64, choices: Vec<Choice>, pescato_intera: fn(), pescato_mezza: fn(), done: fn()) {
    match (i, h) {
        (0, 0) => {
            for choice in choices {
                match choice {
                    Choice::TakeHalf => pescato_mezza(),
                    Choice::TakeInteger => pescato_intera(),
                }
            }
            done()
        },
        (0, h) => elenca_modi_ric(0, h - 1, {let mut v = choices.clone(); v.push(Choice::TakeHalf); v}, pescato_intera, pescato_mezza, done),
        (i, 0) => elenca_modi_ric(i - 1, 1, {let mut v = choices.clone(); v.push(Choice::TakeInteger); v}, pescato_intera, pescato_mezza, done),
        (i, h) => { 
            elenca_modi_ric(i - 1, h + 1, {let mut v = choices.clone(); v.push(Choice::TakeInteger); v}, pescato_intera, pescato_mezza, done);
            elenca_modi_ric(i, h - 1, {let mut v = choices.clone(); v.push(Choice::TakeHalf); v}, pescato_intera, pescato_mezza, done)
        }
    }
}

pub fn elenca_modi(n: i64, pescato_intera: fn(), pescato_mezza: fn(), done: fn())  {
    elenca_modi_ric(n, 0, Vec::new(), pescato_intera, pescato_mezza, done)
}
