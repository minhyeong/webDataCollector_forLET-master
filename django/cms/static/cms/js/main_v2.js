(function() {
    'use strict';

    new Vue({
        el: "#main",
        data: {
            items:[
                {no:1, name:'口から食事ができる', categoryNo:'1'},
                {no:2, name:'自分で動くことができる', categoryNo:'2'},
                {no:3, name:'自分で考えることが', categoryNo:'3'},
                {no:4, name:'自分で呼吸ができる', categoryNo:'4'},
                {no:5, name:'楽しみがある', categoryNo:'1'},
                {no:6, name:'苦痛がない', categoryNo:'2'},
            ],
            rank1:[],
            rank2:[],
            rank3:[],
            rank4:[],
            rank5:[],
            rank6:[]
        },
        computed: {
            myList: {
              get() {
                 return this.items;
              },
              set(value) {
                 this.items = value;
              }
            },
            myRank1: {
              get() {
                 return this.rank1;
              },
              set(value) {
                 this.rank1 = value;
              }
            },
            myRank2: {
              get() {
                 return this.rank2;
              },
              set(value) {
                 this.rank2 = value;
              }
            },
            myRank3: {
              get() {
                 return this.rank3;
              },
              set(value) {
                 this.rank3 = value;
              }
            },
            myRank4: {
              get() {
                 return this.rank4;
              },
              set(value) {
                 this.rank4 = value;
              }
            },
            myRank5: {
              get() {
                 return this.rank5;
              },
              set(value) {
                 this.rank5 = value;
              }
            },
            myRank6: {
              get() {
                 return this.rank6;
              },
              set(value) {
                 this.rank6 = value;
              }
            }
        }
    });
})();
