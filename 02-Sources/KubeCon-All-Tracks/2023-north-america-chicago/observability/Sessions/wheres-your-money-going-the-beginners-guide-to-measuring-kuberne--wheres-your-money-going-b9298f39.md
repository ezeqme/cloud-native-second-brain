---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Mark Poko", "JuanJo Ciarlante", "Grafana Labs"]
sched_url: https://kccncna2023.sched.com/event/1R2vE/wheres-your-money-going-the-beginners-guide-to-measuring-kubernetes-costs-mark-poko-juanjo-ciarlante-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Where%27s+Your+Money+Going%3F+the+Beginners+Guide+to+Measuring+Kubernetes+Costs+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Where's Your Money Going? the Beginners Guide to Measuring Kubernetes Costs - Mark Poko & JuanJo Ciarlante, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Mark Poko, JuanJo Ciarlante, Grafana Labs
- Schedule: https://kccncna2023.sched.com/event/1R2vE/wheres-your-money-going-the-beginners-guide-to-measuring-kubernetes-costs-mark-poko-juanjo-ciarlante-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Where%27s+Your+Money+Going%3F+the+Beginners+Guide+to+Measuring+Kubernetes+Costs+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Where's Your Money Going? the Beginners Guide to Measuring Kubernetes Costs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vE/wheres-your-money-going-the-beginners-guide-to-measuring-kubernetes-costs-mark-poko-juanjo-ciarlante-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Where%27s+Your+Money+Going%3F+the+Beginners+Guide+to+Measuring+Kubernetes+Costs+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8eiLXtL3oLk
- YouTube title: Where's Your Money Going? the Beginners Guide to Measuring Kubernete... Mark Poko & JuanJo Ciarlante
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/wheres-your-money-going-the-beginners-guide-to-measuring-kubernetes-co/8eiLXtL3oLk.txt
- Transcript chars: 32133
- Keywords: cost, cluster, actually, resources, memory, resource, minute, likely, essentially, measure, trying, running, packing, request, understand, pretty, namespace, requests

### Resumo baseado na transcript

welcome um to uh to our talk where's your money going The Beginner's got to monitoring uh measuring kubernetes costs my name is Mark Poco I'm a senior software engineer at graan labs and with me is I'm I'm quano also gra Labs working both we both work at the platform team yes um so before we start let's do a little bit of a story right imagine a scenario you get your Cloud Bill uh your kubernetes cost doubles month over month and uh you're trying to figure out can see that the number is the same but again it's important to understand that it's not continuous what you request especially when when you are running a kubernetes cluster on top of Cloud this will be discrete indeed the noes are being created or

### Excerpt da transcript

welcome um to uh to our talk where's your money going The Beginner's got to monitoring uh measuring kubernetes costs my name is Mark Poco I'm a senior software engineer at graan labs and with me is I'm I'm quano also gra Labs working both we both work at the platform team yes um so before we start let's do a little bit of a story right imagine a scenario you get your Cloud Bill uh your kubernetes cost doubles month over month and uh you're trying to figure out where did your where where did it come from so you start with your bill and you look at it and no matter what you do it doesn't really help you figure out where that cost is coming from so the next thing you do you go to your cost Explorer and see what other dimensions are available for you and really don't come up with much and in this case we're showing um uh what's it called the incidence types you might be able to see where that cost is coming from but nothing about the cluster or the workload so you turn to your favorite uh data visualization tool and you look at things like like CPU usage and memory utilization look at this over time and still nothing's really standing out to you on what is driving our costs and this leaves you sad so show of hands how many people have had this happen before all right that's yeah everybody um how many people are running Cube State metrics in your kubernetes cluster all right so the good news is for those that are doing this you're going to be able to walk away today with some promptu all queries that you could run and be able to visualize this and those that don't hopefully this is a good incentive to maybe look into Cube State Matrix so what can you expect today first thing we're going to do is that there's a we're going to try to show a couple approaches that we use at gra labs to help um Bridge the disconnect between your billing statement and the metrics that you're already collecting in your kubernetes cluster after that we're going to step through a couple of promu examples to help measure um in this particular case we're going to show CPU because that's usually the most costly um and then finally we're going to share a couple of Lessons Learned both in terms of setting this up and measuring it and also uh how we helped improve that cost and with that we turn over to wano so um yeah to to start digging in into this uh we need to understand uh the nature of our our spendings this is a really very simple formula as you can see spend being the amount of mone
