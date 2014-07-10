nosetests --with-cov --cov conn
coverage report
coverage html -d covreport
cd covreport
index.html
cd ..


