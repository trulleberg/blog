Title: Gnuplot Y Value undefined
Date: 2015-06-16
Modified: 2015-06-23
Category: tech
Tags: gnuplot
Slug: gnuplot-y-range-invalid
lang: de
Authors: Hannes Bellmer
Summary: Gnuplot bemängelt das alle Y-Werte ungültig sind.

#### Das Problem
Während ich heute fleißig an meinen Gnuplot Scripten geschaubt habe, bin ich einige male über folgende Fehlermeldung gestolpert:

    :::
    line 0: all points y value undefined!

Da brachte mich doch zum staunen, da das gleiche gnuplot-file vorher einwandfrei funktioniert hatte.

#### Die Lösung
Ich hatte in einem vorherigen Plot mittels ` set xrange [dateA : dateB ] ` die XRANGE angepasst. Mein zweiter Plot war aber in einem anderen Zeitraum und somit gab es hier keine y-werte.


Ich werde die Tage hier mal einen Artikel veröffentlichen wie ich Daten aus [sar](http://sebastien.godard.pagesperso-orange.fr/documentation.html) via [gnuplot](gnuplot.org) visualisiert. ;)
