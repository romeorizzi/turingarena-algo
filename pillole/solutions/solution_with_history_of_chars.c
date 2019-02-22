#include"assert.h"
#define MAXN 30

int num_modi_ric(int n_i, int n_h) {
  assert(n_i >= 0 && n_h >= 0);
  if(n_i == 0)
    return 1;
  if(n_h == 0)
    return num_modi_ric(n_i-1, 1);
  return num_modi_ric(n_i-1, n_h+1) + num_modi_ric(n_i, n_h-1);
}

int num_modi(int n) {
    return num_modi_ric(n, 0);
}


char  history[2*MAXN];
int pos_on_history = 0;


void elenca_modi_ric(int n_i, int n_h, void pescato_intera(), void pescato_mezza(), void done() ) {
  assert(n_i >= 0 && n_h >= 0);
  if(n_i + n_h == 0) {
    for(int move = 0; move < pos_on_history; move++)
      if(history[move]=='M')
	pescato_mezza();
      else
	pescato_intera();
    done();
  }
  else if(n_i == 0) {
    history[pos_on_history++] = 'M';
    elenca_modi_ric(0, n_h-1, pescato_intera, pescato_mezza, done);
    pos_on_history--;
  }
  else if(n_h == 0) {
    history[pos_on_history++] = 'I';
    elenca_modi_ric(n_i-1, 1, pescato_intera, pescato_mezza, done);
    pos_on_history--;
  }
  else {
    history[pos_on_history++] = 'I';
    elenca_modi_ric(n_i-1, n_h+1, pescato_intera, pescato_mezza, done);
    pos_on_history--;
    history[pos_on_history++] = 'M';
    elenca_modi_ric(n_i, n_h-1, pescato_intera, pescato_mezza, done);
    pos_on_history--;
  }
}


void elenca_modi(int n, void pescato_intera(), void pescato_mezza(), void done()) {
  elenca_modi_ric(n, 0, pescato_intera, pescato_mezza, done);
}
