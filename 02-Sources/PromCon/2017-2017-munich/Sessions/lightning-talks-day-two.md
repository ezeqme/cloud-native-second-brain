---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/lightning-talks-day2/
youtube_url: https://www.youtube.com/watch?v=5h-8V5qY2j0
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talks+Day+Two+PromCon+2017
video_match_score: 0.832
status: video-found
---

# Lightning Talks Day Two

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/lightning-talks-day2/
- YouTube: https://www.youtube.com/watch?v=5h-8V5qY2j0

## Resumo

Lightning talks are 5 minutes each. #1 - 50% Cluster Utilization and Beyond with Prometheus Removing the Blindfold with Prometheus Speaker: Stephan Erb Video link - Slides #2 - Instrumenting Java Web Applications without Modifying their Source Code Speaker: Fabian Stäber Video link #3 - Monitoring Blue/Green Deployments with Prometheus Speaker: Darragh Grealish Video link #4 - Monitoring MySQL Replication Delay with mysqld_exporter & pt-heartbeat Speaker: Julien Pivotto Video link #5 -Prometheus in Debian: 2 Years on Speaker: Martín Ferrari Video link - Slides #6 - Monitoring CI/CD Metrics Speaker: Gaurav Kumar Video link #7 - mouldy: Thermo-, Baro-, and Hygrometer with Prometheus Speaker: Nicolai von Neudeck Video link - Slides #8 - Yet Another Prometheus Data Science Tool Speaker: Chris...

## Abstract oficial

Lightning talks are 5 minutes each.



#1 - 50% Cluster Utilization and Beyond with Prometheus

Removing the Blindfold with Prometheus

Speaker: Stephan Erb



Video link -
Slides



#2 - Instrumenting Java Web Applications without Modifying their Source Code

Speaker: Fabian Stäber



Video link



#3 - Monitoring Blue/Green Deployments with Prometheus

Speaker: Darragh Grealish



Video link



#4 - Monitoring MySQL Replication Delay with mysqld_exporter & pt-heartbeat

Speaker: Julien Pivotto



Video link



#5 -Prometheus in Debian: 2 Years on

Speaker: Martín Ferrari



Video link -
Slides



#6 - Monitoring CI/CD Metrics

Speaker: Gaurav Kumar



Video link



#7 - mouldy: Thermo-, Baro-, and Hygrometer with Prometheus

Speaker: Nicolai von Neudeck



Video link -
Slides



#8 - Yet Another Prometheus Data Science Tool

Speaker: Chris Niemira



Video link



#9 - Distributed Blackbox Monitoring

Speaker: Johannes Ziemke



Video link



#10 - kube-state-metrics

What's Missing in Kubernetes Monitoring with Prometheus

Speaker: Frederic Branczyk



Video link -
Slides



#11 - Backing up Prometheus

Speaker: Goutham Veeramachaneni



Video link -
Slides



#12 - Prometheus@Home

Speaker: Richard Hartmann



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/lightning-talks-day2/
- YouTube: https://www.youtube.com/watch?v=5h-8V5qY2j0
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5h-8V5qY2j0
- YouTube title: PromCon 2018: Lightning Talks - Day 2
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/lightning-talks-day-two/5h-8V5qY2j0.txt
- Transcript chars: 39762
- Keywords: prometheus, primitives, wanted, graphite, working, someone, little, configuration, alerts, source, manager, company, basically, actually, write, software, logging, logs

### Resumo baseado na transcript

oh hey uh sir yesterday Stewart my colleague at SoundCloud I gave a talk about alert manager and the life of an alert and he said like someone should totally talk about how to do it in slack and I said yeah do it unfortunately had some beers and I lost so now I give this I'm giving this talk so yeah how to customize here a lot manager notifications actually not really hard and yeah I guess the question most people have like how can I receive nicer select do we configure prometheus we have llamó configuration file and we have like overs which can be included in that file or so common light parameters so with ansible we have like nothing but this nothing with unstable role translates to the one slide to my to my left so you're right and this is basically what is rendered when you are using constable Prometheus roll from cloud load coming and if you want to extend it a little bit we have the same scheme to to your to my

### Excerpt da transcript

oh hey uh sir yesterday Stewart my colleague at SoundCloud I gave a talk about alert manager and the life of an alert and he said like someone should totally talk about how to do it in slack and I said yeah do it unfortunately had some beers and I lost so now I give this I'm giving this talk so yeah how to customize here a lot manager notifications actually not really hard and yeah I guess the question most people have like how can I receive nicer select notifications from alert manager the short answer to that is don't disable slack and use a ticketing system you really don't want to use slack for that it is not at all Tork I will talk about this a little bit more and how to actually do it but to actually give you some aversion or like idea why you really should think about using a ticketing system instead for one keep communication channels like slack for humans and not spam them there's like automatic notifications because at some point no one will beat you a Channel anymore it avoids alerting fatigue we have like some people we receive constantly alerts in that channel and I know that just don't look anymore like when I our sim like hey have you ever looked in this morning they're just like yeah I get so many of them I don't look into them so it really doesn't make sense to use slack for that also you should really consider fixing issues where you get alerts about like in the same way you treat any other work like have a ticket system you assigned someone as assigned to them someone takes care of it you schedule them and your next sprint you can track time you manage us we'll be happy and so on and yeah also like if you get a notification or like an alert which is not really actionable someone do also treat that as a ticket like then look into it like why wasn't actionable and like fix it or like we moved the alert and there is like an integration for alert manager for gyro give them it's like so popular so like you can look into that so if you really still want to use like you can write your own templates in load manager you are not like bound to whatever is the default which might or might not work for you so what you need is you understood llamo as I heard that's really complicated you also need to understand go templating it's also for some people I guess new and not that easy you I guess it helps if you go slack has like a message builder where you can like play around with LexA format you want to have there is an alert manager configuration that
