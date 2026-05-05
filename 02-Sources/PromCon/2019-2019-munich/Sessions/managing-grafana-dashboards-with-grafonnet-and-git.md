---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/managing-grafana-dashboards-with-grafonnet-and-git/
youtube_url: https://www.youtube.com/watch?v=kV3Ua6guynI
youtube_search_url: https://www.youtube.com/results?search_query=Managing+Grafana+Dashboards+with+grafonnet+and+git+PromCon+2019
video_match_score: 0.992
status: video-found
---

# Managing Grafana Dashboards with grafonnet and git

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/managing-grafana-dashboards-with-grafonnet-and-git/
- YouTube: https://www.youtube.com/watch?v=kV3Ua6guynI

## Resumo

Speaker: Adam Wolfe Gordon Grafana is a wonderful tool for visualizing Prometheus data. Getting started with Grafana is simple: login, create a dashboard, add some graphs, and call it a day. Come back later, add some graphs, edit some graphs, hit save and it's all live!

## Abstract oficial

Speaker: Adam Wolfe Gordon

Grafana is a wonderful tool for visualizing Prometheus data. Getting started with Grafana is simple: login, create a dashboard, add some graphs, and call it a day. Come back later, add some graphs, edit some graphs, hit save and it's all live! Flash forward a few months or years and your Grafana instance probably has tens or hundreds of dashboards. Many of them present similar data in slightly inconsistent ways. You can see who last edited a dashboard and why, but it's hard to visualize the changes they made. There's no good way to review changes before they go live like you would for any other code you write. One row on your favorite dashboard is ever so slightly taller than the others and it makes you twitch every time you notice. At DigitalOcean we've solved these problems by storing our dashboard definitions in git, making them human-readable with grafonnet, and updating them via continuous integration. In this talk we'll describe our setup, show how it enables component re-use between dashboards, and demonstrate how it improves the ergonomics of managing Grafana dashboards at scale.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/managing-grafana-dashboards-with-grafonnet-and-git/
- YouTube: https://www.youtube.com/watch?v=kV3Ua6guynI
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kV3Ua6guynI
- YouTube title: PromCon EU 2019: Managing Grafana Dashboards with grafonnet and git
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/managing-grafana-dashboards-with-grafonnet-and-git/kV3Ua6guynI.txt
- Transcript chars: 25931
- Keywords: dashboard, dashboards, little, actually, change, request, metrics, changed, pretty, review, generate, version, variables, create, preview, question, having, changes

### Resumo baseado na transcript

[Music] all right thank you good morning everyone i'm madame wolf gordon i'm a senior engineer to solution where i work on our fenders to communities product i have a since a prank on i'm not going to talk about kubernetes I'm going to talk book or fauna and specifically I'm going to talk about how our team manages our funded dashboards using I get enticing a two o'clock or clinic which I like so I want to start today with a little bit of audience participation so just quick

### Excerpt da transcript

[Music] all right thank you good morning everyone i'm madame wolf gordon i'm a senior engineer to solution where i work on our fenders to communities product i have a since a prank on i'm not going to talk about kubernetes I'm going to talk book or fauna and specifically I'm going to talk about how our team manages our funded dashboards using I get enticing a two o'clock or clinic which I like so I want to start today with a little bit of audience participation so just quick show of hands how many of you use graph on alright that's like almost everyone ideas anyone doesn't know worker fun is refine a is a visualization system lets you build dashboards supports Prometheus supports lots of other metrics backends as well as logs and various other things the nice thing will crow fauna is lets you see a lot of data in one place lets you pull in metrics from multiple sources into a single dashboard yeah it saves you from having to remember a bunch of prompt deliveries for metrics that you use a lot how many of you is sacred fauna is important to important to your operations alright a lot of us it's definitely important for us at digitalocean if something goes wrong if I get paged in the middle of the night Griffin is one of the first places I go and look to see maybe what's going on what am I getting paged for if I deploy something and I'm not totally confident in its performance characteristics I go find is where I'm gonna go and look watch make sure this look good how many of you do code review for your application or service whatever it is you're building almost differently most people how many of you do some kind of CI testing for your services how many do some kind of just continuous deployment so quite a few of us I think these are all you know pretty commonly accepted engineering practices now in an industry most of us review our code before it's committed most of us test it before it's committed most of us deploy right now once it's once it is committed how many of you do code review and CI testing and continuous deployment for your family dashboards all right there's a few that's good so some of us but not a lot of us most of us are doing it for our applications in our services but not for our girls and we weren't either but we decided that we should we remember we said our defended efforts are important to us they're important part of our operations so we should apply good engineering practices to them we should keep them in version control so that we
