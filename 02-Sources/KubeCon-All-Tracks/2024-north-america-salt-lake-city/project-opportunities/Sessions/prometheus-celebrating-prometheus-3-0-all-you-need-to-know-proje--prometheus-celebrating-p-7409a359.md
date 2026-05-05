---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Observability"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8b/prometheus-celebrating-prometheus-30-all-you-need-to-know-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus%3A+Celebrating+Prometheus+3.0%3A+All+You+Need+To+Know%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Prometheus: Celebrating Prometheus 3.0: All You Need To Know! | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8b/prometheus-celebrating-prometheus-30-all-you-need-to-know-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus%3A+Celebrating+Prometheus+3.0%3A+All+You+Need+To+Know%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Prometheus: Celebrating Prometheus 3.0: All You Need To Know! | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8b/prometheus-celebrating-prometheus-30-all-you-need-to-know-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Prometheus%3A+Celebrating+Prometheus+3.0%3A+All+You+Need+To+Know%21+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jcDtB150inI
- YouTube title: Prometheus: Celebrating Prometheus 3.0: All You Need To Know! | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/prometheus-celebrating-prometheus-3-0-all-you-need-to-know-project-lig/jcDtB150inI.txt
- Transcript chars: 5694
- Keywords: metric, version, metrics, protocol, storage, amazing, histograms, enables, recommend, characters, prometheus, solution, instrumentation, called, notice, understand, enabled, remote

### Resumo baseado na transcript

I've been told we are a little bit early but I think we can slowly start in hello everyone my name is BK bka I work at Google and I'm also promus maintainer and in the next 5 minutes I will have a pleasure to share some all you need to know about what's new in the prus project as you know pritus is a graduated cncf project that is all in solution end to end solution for your metrics and monitoring right with collection instrumentation storage quering and alerting

### Excerpt da transcript

I've been told we are a little bit early but I think we can slowly start in hello everyone my name is BK bka I work at Google and I'm also promus maintainer and in the next 5 minutes I will have a pleasure to share some all you need to know about what's new in the prus project as you know pritus is a graduated cncf project that is all in solution end to end solution for your metrics and monitoring right with collection instrumentation storage quering and alerting and there is a lot of a lot to cover um this week because after seven years this week we are releasing a new major version of PRS called freezero so let's dive in and you know there are many many things to discuss but first thing that are is is would you notice when you would install a new pruse version is a new refreshed UI and you know it's faster it's more lean it's uh more responsive it feels and looks more modern but it are also you know amazing features inside um there is promql teview and quer explanation page H and there's also a metric and label Explorer all of those will help you to really access understand and explore your metrics but also from Co queries so it's all built in into the news new version enabled by default to power this UI we also have uh worked together to release a new second version of the you know our metric streaming protocol called remote right so the 20 Tri comes with more capabilities to essentially send more data along your samples um being metadata you know histograms uh and exemplars but it do it does it all by also making the protocol more reliable especially for part partial errors and also more efficient thanks to the novel string interning mechanism so enables more by costing less which is amazing so the next thing will get you excited if you are fan of open Telemetry and you want to really send openet traffic to prome and really use the same openet metric format um for you we kind of like in the free zero version we have a new OTP receiver which is improved and it works well with outof order support in pruse which we recommend to enabling because of the nature of OTP or generally metric pushes and we also kind of recommend and give you best practice but really configuration to attach certain resource attributes that we recommend uh to to all your metrics and maybe those veror ones you put into a special Target info label metric that you can then join on the query uh promel query later um but to really stay um you know and and for the best exper experience f
