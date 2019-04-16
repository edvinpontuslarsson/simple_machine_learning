def get_index_view(msg):
    return '''
        <h3>{0}</h3>
        <form method="POST">
            Enter the weight (in grams) of the animal:
            <input type="text" name="weight" /><br />
            Can the animal fly:
            <input type="radio" name="can-fly" value="yes" /> Yes 
            <input type="radio" name="can-fly" value="no" /> No
            <p><input type="submit" value="Submit" /></p>
        </form>
    '''.format(msg)