var Nav = $.Class.create({
    sections: {
        'dashboard': ViewDashboard,
        'internal': ViewInternal,
    },
    init: function(name){
        info('Init Nav');
        this.to();
    },
    to: function(section){
        var section = $('body').attr('id');
        if (this.sections[section] == undefined){
            error('View not found '+section);
            return;
        }
        info('Go to '+section);
        this.section = new this.sections[section];
    },
    base: function(){

    }
});

function log(m){
    if(window.console != undefined) return console.log(m);
}

function info(m){
    if(window.console != undefined) return console.info(m);
}

function error(m){
    if(window.console != undefined) return console.error(m);
}

var nav;
$(window).ready(function() {
    info('Dom Load');
    nav = new Nav();
});