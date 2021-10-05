from flask import Blueprint,render_template
auth=Blueprint( __name__,"auth")

@auth.route('/compare')
def compare():
    return render_template("compare.html")