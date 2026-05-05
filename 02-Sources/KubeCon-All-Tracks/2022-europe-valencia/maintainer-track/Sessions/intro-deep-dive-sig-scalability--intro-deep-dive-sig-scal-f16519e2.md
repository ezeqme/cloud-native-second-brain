---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Marcel Zięba", "Wojciech Tyczyński", "Google"]
sched_url: https://kccnceu2022.sched.com/event/ytsB/intro-+-deep-dive-sig-scalability-marcel-zieba-wojciech-tyczynski-google
youtube_search_url: https://www.youtube.com/results?search_query=Intro+%2B+Deep+Dive%3A+SIG+Scalability+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Intro + Deep Dive: SIG Scalability - Marcel Zięba & Wojciech Tyczyński, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Marcel Zięba, Wojciech Tyczyński, Google
- Schedule: https://kccnceu2022.sched.com/event/ytsB/intro-+-deep-dive-sig-scalability-marcel-zieba-wojciech-tyczynski-google
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+%2B+Deep+Dive%3A+SIG+Scalability+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Intro + Deep Dive: SIG Scalability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytsB/intro-+-deep-dive-sig-scalability-marcel-zieba-wojciech-tyczynski-google
- YouTube search: https://www.youtube.com/results?search_query=Intro+%2B+Deep+Dive%3A+SIG+Scalability+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H123tJMnbmA
- YouTube title: Intro + Deep Dive: SIG Scalability - Marcel Zięba, Google
- Match score: 0.836
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/intro-deep-dive-sig-scalability/H123tJMnbmA.txt
- Transcript chars: 27521
- Keywords: actually, scalability, cluster, basically, latency, number, regressions, running, question, performance, startup, control, happening, testing, usually, regression, limits, second

### Resumo baseado na transcript

um my name is Marcel genba and I'm software engineer at Google and I'm also one of the two chairs of sex scalability and today we'll be talking about sex scalability introduction that also Deep dive so first question that we need to answer is what we do as a sex scalability six scalability is a bit different from other six because we do not own we do not own production code we only own test code that we use for testing the scalability of kubernetes so basically we do

### Excerpt da transcript

um my name is Marcel genba and I'm software engineer at Google and I'm also one of the two chairs of sex scalability and today we'll be talking about sex scalability introduction that also Deep dive so first question that we need to answer is what we do as a sex scalability six scalability is a bit different from other six because we do not own we do not own production code we only own test code that we use for testing the scalability of kubernetes so basically we do have five areas five areas that we are interested in in terms of scalability so first of all the most important is actually defining what the scalability is and once we know what the scalability means which will I which I will explain later and we also want to set up some goals so you can think of it as you know we could start improving the kubernetes by making some improvements but it doesn't matter if the end user is not able to see those improvements and actually have some Better scalability Properties except for defining and driving those goals we also contribute to kubernetes in a way that we want to make kubernetes more scalable so what we do is we usually coordinate between six or or ask other states to actually make some improvements in order to make kubernetes more scalable but okay let's say that we we do have those goals in mind for kubernetes that we want to achieve but first of all we need to measure and monitor how the performance and scalability of kubernetes actually changes over time um you probably know that every day there are multiple PR's merged into kubernetes and each of these PRS features these changes can potentially impact the performance of the whole kubernetes so that's why one of the most important areas of six scalability is actually monitoring the performance of kubernetes to make sure that we do not regress which is actually the next next Point here so basically once we have this monitoring then we are able to track different metrics and see if there is any regression and and last but not least we also consult and Coach other six so probably most of you know that there are caps which cap is kind of like design Dock and when you are when you want to implement new feature there are some sections that are specific to six scalability and with questions like how does your feature impact um control plane or what kind of calls is making your uh making your feature that are additional to the previous state and so one more important part is not to confuse wait a second o
