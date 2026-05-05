---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Phillip Kuznetsov", "New Relic"]
sched_url: https://kccncna2022.sched.com/event/182IS/when-the-logs-just-dont-cut-it-root-causing-incidents-without-re-deploying-prod-phillip-kuznetsov-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=When+the+Logs+Just+Don%E2%80%99t+Cut+It%3A+Root-Causing+Incidents+Without+Re-Deploying+Prod+CNCF+KubeCon+2022
slides: []
status: parsed
---

# When the Logs Just Don’t Cut It: Root-Causing Incidents Without Re-Deploying Prod - Phillip Kuznetsov, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Phillip Kuznetsov, New Relic
- Schedule: https://kccncna2022.sched.com/event/182IS/when-the-logs-just-dont-cut-it-root-causing-incidents-without-re-deploying-prod-phillip-kuznetsov-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=When+the+Logs+Just+Don%E2%80%99t+Cut+It%3A+Root-Causing+Incidents+Without+Re-Deploying+Prod+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre When the Logs Just Don’t Cut It: Root-Causing Incidents Without Re-Deploying Prod.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182IS/when-the-logs-just-dont-cut-it-root-causing-incidents-without-re-deploying-prod-phillip-kuznetsov-new-relic
- YouTube search: https://www.youtube.com/results?search_query=When+the+Logs+Just+Don%E2%80%99t+Cut+It%3A+Root-Causing+Incidents+Without+Re-Deploying+Prod+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QCABjMm5JpA
- YouTube title: When the Logs Just Don’t Cut It: Root-Causing Incidents Without Re-Deploying Prod- Phillip Kuznetsov
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/when-the-logs-just-dont-cut-it-root-causing-incidents-without-re-deplo/QCABjMm5JpA.txt
- Transcript chars: 23336
- Keywords: trace, actually, running, little, production, kernel, specify, function, ebpf, specific, values, access, script, deploy, logs, another, security, program

### Resumo baseado na transcript

uh hello everyone my name is Philip kuznetsov and I will be presenting a root causing incidents without redeploying prod a little bit about me I am a software engineer at New Relic where I spend most of my time building pixie um let's just jump right into it so here's the situation imagine we're working at an e-commerce company called online boutique we're selling a bunch of hip trendy items and things have been chugging on chugging along pretty well recently we've had no problems code is shipping everything's

### Excerpt da transcript

uh hello everyone my name is Philip kuznetsov and I will be presenting a root causing incidents without redeploying prod a little bit about me I am a software engineer at New Relic where I spend most of my time building pixie um let's just jump right into it so here's the situation imagine we're working at an e-commerce company called online boutique we're selling a bunch of hip trendy items and things have been chugging on chugging along pretty well recently we've had no problems code is shipping everything's great until today the front-end service is panicking something is happening there that we don't really know what's going on we what's worse is we haven't released code to the front-end service in weeks so there's no way that any changes in the front-end service are responsible this is a classic problem in microservices you have dependency trees across multiple different services that when one thing changes in one service causes a break in another service so one thing we did change recently which we highly suspect is the problem uh we recently added this new product item called uh sticker a simple online boutique sticker and we don't know why this is causing us any problems the search so we're looking at the logs and we see this one log with the Panic that says one of the specified money values is invalid it's a bit weird when our money values is weird Okay we keep seeing this error and it keeps getting returned by this sum function um before I dive a little bit deeper into what the sum function is you should understand why we need to have a sum function in the first place why don't we just add these together the way money is represented inside of our service let me jump ahead it's uh split up into the units section and a nano section the units is the values before the decimal point the Nanos are the values after the decimal point but represented as Nano units so a billion Nano units are one unit unfortunately whenever we see this error from the sum function we don't know what value is actually invalid it's it's like what is actually causing this problem a valid money type as I mentioned before is one that uh has matching signs between the units and the Nanos so both positive or both negative and that the value that the Nanos are in absolute value less than a billion for some reason some value showing up through our system is not matching one of these conditions or both of these conditions unfortunately it's not that easy to tell what happened in our
