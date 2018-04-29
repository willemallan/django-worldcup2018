var ViewDashboard = BaseView.extend({
    init: function(){
        this._super();
        log('Init Admin Dashboard');
        this.bind_events();
    },
    bind_events: function(){
    }
});

var ViewInternal = BaseView.extend({
    init: function(){
        this._super();
        log('Init Admin Internal');
        this.bind_events();
    },
    bind_events: function(){
    }
});