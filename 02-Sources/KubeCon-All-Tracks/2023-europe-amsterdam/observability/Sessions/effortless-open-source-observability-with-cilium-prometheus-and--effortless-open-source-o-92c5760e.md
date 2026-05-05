---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability", "Networking", "Community Governance"]
speakers: ["Raymond de Jong", "Anna Kapuścińska", "Isovalent"]
sched_url: https://kccnceu2023.sched.com/event/1HyYo/effortless-open-source-observability-with-cilium-prometheus-and-grafana-lgtm-raymond-de-jong-anna-kapuscinska-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Effortless+Open+Source+Observability+with+Cilium%2C+Prometheus+and+Grafana+-+LGTM%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Effortless Open Source Observability with Cilium, Prometheus and Grafana - LGTM! - Raymond de Jong & Anna Kapuścińska, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Raymond de Jong, Anna Kapuścińska, Isovalent
- Schedule: https://kccnceu2023.sched.com/event/1HyYo/effortless-open-source-observability-with-cilium-prometheus-and-grafana-lgtm-raymond-de-jong-anna-kapuscinska-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Effortless+Open+Source+Observability+with+Cilium%2C+Prometheus+and+Grafana+-+LGTM%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Effortless Open Source Observability with Cilium, Prometheus and Grafana - LGTM!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYo/effortless-open-source-observability-with-cilium-prometheus-and-grafana-lgtm-raymond-de-jong-anna-kapuscinska-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Effortless+Open+Source+Observability+with+Cilium%2C+Prometheus+and+Grafana+-+LGTM%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=njnhdtAykiA
- YouTube title: Effortless Open Source Observability with Cilium, Prometheus, and Grafana - LGTM!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/effortless-open-source-observability-with-cilium-prometheus-and-grafan/njnhdtAykiA.txt
- Transcript chars: 29700
- Keywords: network, policy, metrics, everything, inside, kernel, enterprise, cluster, psyllium, deploy, networking, ebpf, understand, another, request, developer, cinema, related

### Resumo baseado na transcript

um so let's start by the beginning so who am I um so as you can guess by my accents I'm not coming from here um so that will be in English but with a French accent otherwise it's too easy if you don't understand something feel free ask me to repeat I won't take it personally I'm used to it I'm 30 I'm 30 years old so um I heard that many times already I work at I surveillance I'm going to talk a little bit after about what

### Excerpt da transcript

um so let's start by the beginning so who am I um so as you can guess by my accents I'm not coming from here um so that will be in English but with a French accent otherwise it's too easy if you don't understand something feel free ask me to repeat I won't take it personally I'm used to it I'm 30 I'm 30 years old so um I heard that many times already I work at I surveillance I'm going to talk a little bit after about what we do before joining is Overland I work at Google I did kubernetes things I'm still contributing for kubernetes on auto scanning and networking Sig I've done a lot for cluster Auto scanning and Gateway API recently at isovan and my job is what we call the sales engineer solution architect so I help our customer using celium ebpf and silium Enterprise so today I'm gonna talk a lot but if you have questions feel free to raise your hand we have like a manageable number of people so you don't have to wait for the end if it's like a small thing like oh I don't understand how does that work if it's personal regarding your use case then it's better to wait for the end every time I say psyllium during the presentation it's Cinema SS so let's keep it transparent every time I say psyllium it's CM OSS if there is something in the presentation related to CM Enterprise so what we do at isotherland I will always mention it so I will say CDM Enterprise I have to because some of the demo and stuff I want to show to you are very linked to that and I want you to understand like the under the hood architecture of things so I have to use the Enterprise version but every time there is something that is Enterprise only I will always told you so Syrian Cinema it says Cinema Enterprise is what we do at i7 and evpf we're going to talk about ebpf first who have never heard about kubernetes before all right who is not using kubernetes in production okay okay so not that much people who have never heard about psyllium before okay who is using Cinema in production okay ebpf who has never heard about ebpf before okay who is using evpf in production all right it's still a few people okay who is a Linux kernel developer all right that one always on point okay very sorry for the few people who already heard that one that you know it's working um okay so let's start start with the beginning um so I'm gonna do two things I'm gonna move from slide to drawing I have the drawing skills of a two years old so don't blame me but it's it's helpful to explain like very hard conten
