var AUTH0_CLIENT_ID = $('body').data('auth0_client_id');
var AUTH0_DOMAIN = $('body').data('auth0_domain');
var AUTH0_CALLBACK_URL = $('body').data('auth0_callback_url')

var lock = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, {
    auth: {
        redirectUrl: AUTH0_CALLBACK_URL,
        responseType: 'code',
        params: {
            scope: 'openid email'
        }
    }
});

$('.login button').click(function(){
    lock.show();
})
