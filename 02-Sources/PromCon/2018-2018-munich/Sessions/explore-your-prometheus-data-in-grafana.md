---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/explore-your-prometheus-data-in-grafana/
youtube_url: https://www.youtube.com/watch?v=mIfjBcjAEyE
youtube_search_url: https://www.youtube.com/results?search_query=Explore+Your+Prometheus+Data+in+Grafana+PromCon+2018
video_match_score: 0.987
status: video-found
---

# Explore Your Prometheus Data in Grafana

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/explore-your-prometheus-data-in-grafana/
- YouTube: https://www.youtube.com/watch?v=mIfjBcjAEyE

## Resumo

Speaker: David Kaltschmidt Grafana is the de-facto dashboarding solution for Prometheus. Now imagine you received a page. Grafana is often the starting point for your incident response.

## Abstract oficial

Speaker: David Kaltschmidt

Grafana is the de-facto dashboarding solution for Prometheus. Now imagine you received a page. Grafana is often the starting point for your incident response. You look at a time series panel, form a hypothesis, and would like to dive deeper. We've built a whole new section that allows you to do just that by iterating quickly through Prometheus queries while leaving your dashboards intact. I'll show-case our new Explore UI and how it can fit into your workflows for both troubleshooting and data exploration.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/explore-your-prometheus-data-in-grafana/
- YouTube: https://www.youtube.com/watch?v=mIfjBcjAEyE
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mIfjBcjAEyE
- YouTube title: PromCon 2018: Explore Your Prometheus Data in Grafana
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/explore-your-prometheus-data-in-grafana/mIfjBcjAEyE.txt
- Transcript chars: 18923
- Keywords: basically, another, prometheus, queries, change, actually, quickly, anyway, little, dashboard, dashboards, always, pretty, question, around, recording, allows, compare

### Resumo baseado na transcript

yeah I'm not call called cars usually here he is on parental leave right now which is funny because last year he just got back from parental leave and but this year he has twins or he's getting twins so big applause for Carl because I think he's gonna have a lot of a lot of work on his hands and but also on a more serious and I really want to encourage people to go on parental leave I personally regret that I haven't gone on leave when my

### Excerpt da transcript

yeah I'm not call called cars usually here he is on parental leave right now which is funny because last year he just got back from parental leave and but this year he has twins or he's getting twins so big applause for Carl because I think he's gonna have a lot of a lot of work on his hands and but also on a more serious and I really want to encourage people to go on parental leave I personally regret that I haven't gone on leave when my son was born so I think it's important that people in tech like take yes take advantage of this yeah all right so I guess you're stuck with me now I am responsible for UX things but speaking of stuck if you click somewhere in Gravano and don't get any further then you just reach out to me David Geffen or calm or on Twitter so what is Cortana fun as a currently on a journey on a transition from dashboarding solution to observability platform and I'll show a bit later how that what that looks like and as big so first we're gonna do a quick overview on what happened between the last prom Kong a year ago to now and the most obvious is the light theme that you see there which personally I think is more is easy on eyes it's also more sellable to enterprise which is nice but I've had someone come up to me and say it can you make the light just a bit so because I really want people to stick to the dark to dark on so I'm not sure if we can like accommodate this bear let's see so on the on the on the on the back there you also see the the folders that's also new so you can group your your your dashboards by folders and folders can also have permissions so I think that's quite neat and then also lo and behold people were probably using this now for quite a while but that was also introduced in the last year which is the instant query which allows you to only query the last data point and that is quite nice if especially if the queries are quite expensive and you only really want to see the the last value and it's also best displayed in a table panel there also speaking of table panels we implemented another thing there basically if if you have multiple queries you can still render them in a table and it's trying to match the rows that have the same the same label value so in this case there's a breakdown by namespace and all of these values will end up in the same or the values that are the responses that have the same namespace will end up in the same roast and I think it's quite neat to compare to compare it's a completely to comp
