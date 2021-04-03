export default (context) => {
    if (!context.app.context.app.$cookies.get('token')) {
        return context.redirect('/login')
    }
}