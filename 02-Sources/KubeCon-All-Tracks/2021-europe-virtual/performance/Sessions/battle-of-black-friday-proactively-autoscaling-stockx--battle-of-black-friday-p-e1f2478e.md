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
themes: ["SRE Reliability"]
speakers: ["Mario Loria", "Carta", "Kyle Schrade", "StockX"]
sched_url: https://kccnceu2021.sched.com/event/iE2T/battle-of-black-friday-proactively-autoscaling-stockx-mario-loria-carta-kyle-schrade-stockx
youtube_search_url: https://www.youtube.com/results?search_query=Battle+of+Black+Friday%3A+Proactively+Autoscaling+StockX+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Battle of Black Friday: Proactively Autoscaling StockX - Mario Loria, Carta & Kyle Schrade, StockX

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Mario Loria, Carta, Kyle Schrade, StockX
- Schedule: https://kccnceu2021.sched.com/event/iE2T/battle-of-black-friday-proactively-autoscaling-stockx-mario-loria-carta-kyle-schrade-stockx
- Busca YouTube: https://www.youtube.com/results?search_query=Battle+of+Black+Friday%3A+Proactively+Autoscaling+StockX+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Battle of Black Friday: Proactively Autoscaling StockX.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2T/battle-of-black-friday-proactively-autoscaling-stockx-mario-loria-carta-kyle-schrade-stockx
- YouTube search: https://www.youtube.com/results?search_query=Battle+of+Black+Friday%3A+Proactively+Autoscaling+StockX+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IqrKFBxf_Dk
- YouTube title: Battle of Black Friday: Proactively Autoscaling StockX - Mario Loria, Carta & Kyle Schrade, StockX
- Match score: 0.816
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/battle-of-black-friday-proactively-autoscaling-stockx/IqrKFBxf_Dk.txt
- Transcript chars: 32458
- Keywords: traffic, actually, scaling, little, barricade, cluster, stockx, around, autoscaler, enough, everybody, course, massive, requests, trying, definitely, everything, normally

### Resumo baseado na transcript

well hello everybody welcome to kubecon eu uh my name is kyle um i'm here with mario as well and we're here to talk to you kind of about our story of the battle of black friday in proactive and reactive auto scaling at stockx um before we start we kind of want to introduce ourselves and introduce stockx a little bit so some of this stuff makes a little bit more sense when we're walking through it uh like i said my name is kyle i'm a senior software

### Excerpt da transcript

well hello everybody welcome to kubecon eu uh my name is kyle um i'm here with mario as well and we're here to talk to you kind of about our story of the battle of black friday in proactive and reactive auto scaling at stockx um before we start we kind of want to introduce ourselves and introduce stockx a little bit so some of this stuff makes a little bit more sense when we're walking through it uh like i said my name is kyle i'm a senior software engineer at stockx um i like graphql probably just a little too much if you guys ever want to talk about it our twitter handles are in the lower right-hand side feel free to hit me about anything graphql um i've talked at a few other conferences about it it's a fun passion of mine and mario do you want to give yourself a little intro of course i do thank you kyle i'm mario lauria i actually just love stockx a few months ago uh for carda i'm a yama aficionado uh devops sre engineer i love everything infrastructure of course love kubernetes and auto scaling is one of the funnest challenges and kyle and i have a lot to discuss today it's going to be a fun session so cool so uh like we mentioned this happened at stockx a lot of the stuff is based off of work we did at stockx stockx is a stock market of things we are a live bid and ask model where people will actively bid and ask things just like a stock market but instead of trading stocks they will trade normally some type of product so in the normal instance the stuff that most people know is some type of jordan or some type of nike card we just expanded to collectibles so trading cards are a big thing that we do now as well we also do some electronics but again it's that live stock model where people will be actively asking for something and bidding on something and when they match that's when you get your item so the first thing we want to do is we want to really frame this problem of what was our problem that we had to solve and what is this battle that we had and the big thing is is it's the surges in traffic our traffic is very unnormal so like a lot of places you would expect you know your traffic to go up through the day and down at night and kind of follow that nice little easy wave uh we don't have that unfortunately we have these very very spiky trends where all of a sudden kanye will feel like he needs to drop a shoe and all of a sudden all of our stuff tanks and we go you know from zero request to a million request almost instantly and that's kind of w
