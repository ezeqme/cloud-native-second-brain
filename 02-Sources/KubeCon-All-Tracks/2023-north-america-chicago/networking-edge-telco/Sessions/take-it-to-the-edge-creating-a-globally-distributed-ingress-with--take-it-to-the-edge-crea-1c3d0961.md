---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Networking + Edge + Telco"
themes: ["Networking"]
speakers: ["Jimmi Dyson", "D2iQ"]
sched_url: https://kccncna2023.sched.com/event/1R2o5/take-it-to-the-edge-creating-a-globally-distributed-ingress-with-istio-k8gb-jimmi-dyson-d2iq
youtube_search_url: https://www.youtube.com/results?search_query=Take+It+to+the+Edge%3A+Creating+a+Globally+Distributed+Ingress+with+Istio+%26+K8gb+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Take It to the Edge: Creating a Globally Distributed Ingress with Istio & K8gb - Jimmi Dyson, D2iQ

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Jimmi Dyson, D2iQ
- Schedule: https://kccncna2023.sched.com/event/1R2o5/take-it-to-the-edge-creating-a-globally-distributed-ingress-with-istio-k8gb-jimmi-dyson-d2iq
- Busca YouTube: https://www.youtube.com/results?search_query=Take+It+to+the+Edge%3A+Creating+a+Globally+Distributed+Ingress+with+Istio+%26+K8gb+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Take It to the Edge: Creating a Globally Distributed Ingress with Istio & K8gb.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2o5/take-it-to-the-edge-creating-a-globally-distributed-ingress-with-istio-k8gb-jimmi-dyson-d2iq
- YouTube search: https://www.youtube.com/results?search_query=Take+It+to+the+Edge%3A+Creating+a+Globally+Distributed+Ingress+with+Istio+%26+K8gb+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4qJDkw5YGqM
- YouTube title: Take It to the Edge: Creating a Globally Distributed Ingress with Istio & K8gb - Jimmi Dyson, D2iQ
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/take-it-to-the-edge-creating-a-globally-distributed-ingress-with-istio/4qJDkw5YGqM.txt
- Transcript chars: 35765
- Keywords: ingress, address, gateway, stateful, anyway, happens, europe, external, cluster, deployed, addresses, website, running, actually, failure, internet, another, brilliant

### Resumo baseado na transcript

it's always fun watching the countdown timer going like oh 10 nine turn in your head it's really fun thank you for coming um my name is Jimmy I I work at a company called D2 IQ um I'm principal architect principal engineer there um been working with kubernetes for I don't know seven eight years something like that um across lots of it mainly in the ecosystem rather than core kubernetes um so I love all the cncf projects that we've got I love putting them together building up that a lot in my life um it's a great phrase but D DNS also has some amazing abilities that we that we can use right so learning about DNS learning about something that is so old in the animals of time learning about it learning how to use it for your benefit rather than thinking about creating something new is really you know where we're going to go and we're going to we're going to use some real key principles of DNS through some of the projects when we

### Excerpt da transcript

it's always fun watching the countdown timer going like oh 10 nine turn in your head it's really fun thank you for coming um my name is Jimmy I I work at a company called D2 IQ um I'm principal architect principal engineer there um been working with kubernetes for I don't know seven eight years something like that um across lots of it mainly in the ecosystem rather than core kubernetes um so I love all the cncf projects that we've got I love putting them together building up um Solutions from them and and contributing to them and building stuff around it so we're going to talk um today about uh a distributed Ingress so I I've been working with cumor a long time and I'm sure you you do you all work with cetes but yeah vast majority so I saw waving that's great I like that not just put a hand up give it a good wave yes um and quite often when we talk about we talk about a single cluster we're talking about we deploy our apps to a single cluster and maybe we deploy it to other clusters but the kind of multicluster discussion is isn't solved yet I think there's loads of opportunity Upstream um I used to be the maintainer of cube fed which was Federation V2 in in kubernetes before we archived it um and there's loads of scope in Sig multicluster if if you want to do stuff there by the way there's loads of stuff around multic clustering that that we need to to fix in the and improve in the kubernetes ecosystem so we talk about distributed Ingress and what I mean by a distributed Ingress is I want users to not know that they're talking to multiple clusters I want our users that are accessing our applications whether that's your internal applications on your your internets or whatever or over the Internet or whatever I want the user to be completely ignorant of where that's running um and I want to make it as seamless a kind of experience as possible including stuff like fail overing including stuff like how do how do we deal with faults how do we deal with stuff like stateful Services um and we're going to go through another one this this talk actually came just from a chat with someone who's learning kubernetes and they were going I've got a website it's just a little website um just just one and it's just some static pages and I I I want to know how how do I let people access it that wasn't their voice by the way they've got a very lovely voice not like mine anyway I hate hearing my voice um so I've got a website okay you've got a website and you want to expose
