---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Saiyam Pathak", "Civo", "Karthik Gaekwad", "Verica"]
sched_url: https://kccnceu2021.sched.com/event/iE2H/power-level-9000-improving-application-performance-with-chaos-engineering-saiyam-pathak-civo-karthik-gaekwad-verica
youtube_search_url: https://www.youtube.com/results?search_query=Power+Level+9000%21+Improving+Application+Performance+with+Chaos+Engineering+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Power Level 9000! Improving Application Performance with Chaos Engineering - Saiyam Pathak, Civo & Karthik Gaekwad, Verica

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Saiyam Pathak, Civo, Karthik Gaekwad, Verica
- Schedule: https://kccnceu2021.sched.com/event/iE2H/power-level-9000-improving-application-performance-with-chaos-engineering-saiyam-pathak-civo-karthik-gaekwad-verica
- Busca YouTube: https://www.youtube.com/results?search_query=Power+Level+9000%21+Improving+Application+Performance+with+Chaos+Engineering+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Power Level 9000! Improving Application Performance with Chaos Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2H/power-level-9000-improving-application-performance-with-chaos-engineering-saiyam-pathak-civo-karthik-gaekwad-verica
- YouTube search: https://www.youtube.com/results?search_query=Power+Level+9000%21+Improving+Application+Performance+with+Chaos+Engineering+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=btGFt5-37hs
- YouTube title: Power Level 9000! Improving Application Performance with Chaos Engineering - S. Pathak & K. Gaekwad
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/power-level-9000-improving-application-performance-with-chaos-engineer/btGFt5-37hs.txt
- Transcript chars: 28293
- Keywords: workflow, cluster, litmus, engineering, application, actually, running, experiment, flux, repository, experiments, create, workflows, network, github, deploy, production, components

### Resumo baseado na transcript

all right well folks welcome to our presentation on power leveling over 9000 improving application performance with some chaos engineering hello everyone uh uh i am sayyam pathak director of technical evangelism at ceo building the next-gen simplified kubernetes service on sibo i'm a cncf ambassador and influx ace i'm author of learn cks scenarios which is published on road based on practicing kubernetes cks certification yes i am cka ckad and cks certified and i organize few of the meetups at bangalore i run a youtube channel where i

### Excerpt da transcript

all right well folks welcome to our presentation on power leveling over 9000 improving application performance with some chaos engineering hello everyone uh uh i am sayyam pathak director of technical evangelism at ceo building the next-gen simplified kubernetes service on sibo i'm a cncf ambassador and influx ace i'm author of learn cks scenarios which is published on road based on practicing kubernetes cks certification yes i am cka ckad and cks certified and i organize few of the meetups at bangalore i run a youtube channel where i talk about all things cloud native and uh you can reach me on twitter anytime address i am product and i'm karthik wadd i'm the head of cloud native engineering uh over here at verica and lately in the last uh probably eight months or so i've been doing a lot of work in the chaos engineering space building chaos engineering verifications um i've written the learning kubernetes and other cloud native courses on linkedin learning i used to manage the oracle kubernetes engine over at oracle cloud and also do a bunch of things uh in the devops and cloud space here in austin texas you can find me on twitter at aerationone so let's talk about the storyline today so we'll do a quick overview of the state of the cloud native universe figure out where chaos engineering fits in and then kind of talk about what we mean by kiosk engineering its intersection with cloud native and then the most important part the demos of course and finally we'll go into some speaker recommendations at the end so state of the universe um so i'm a big fan uh and i'm kind of a nerd when it comes to looking at reports and things like that so um this the state of our world is we're kind of going to a multi-cloud world we've known this for a while but you know in the research report from 451 research uh this is kind it's a little bit older uh came out in 2018 2019 that time frame but it said 67 percent of enterprises will have multi-cloud or hybrid it environments by 2019 um but you know with greater choice brings more complexity uh we saw this again in the cncf report that came out last year where 26 of uh usage uh is actually multi-cloud so that's grown a lot from years past which uh if you notice in the graph you know there was nothing in 20 uh 2019 but 2020 that's uh that's a brand new thing there's also increased container usage so this is no surprise for to anybody the use of containers and production is that has become the norm today for the server surve
