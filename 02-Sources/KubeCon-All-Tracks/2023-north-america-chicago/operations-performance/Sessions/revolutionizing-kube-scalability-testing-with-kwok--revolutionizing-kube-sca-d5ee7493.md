---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Wei Huang", "Weiwei Yang", "Apple"]
sched_url: https://kccncna2023.sched.com/event/1R2ub/revolutionizing-kube-scalability-testing-with-kwok-wei-huang-weiwei-yang-apple
youtube_search_url: https://www.youtube.com/results?search_query=Revolutionizing+Kube+Scalability+Testing+with+KWOK+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Revolutionizing Kube Scalability Testing with KWOK - Wei Huang & Weiwei Yang, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Wei Huang, Weiwei Yang, Apple
- Schedule: https://kccncna2023.sched.com/event/1R2ub/revolutionizing-kube-scalability-testing-with-kwok-wei-huang-weiwei-yang-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Revolutionizing+Kube+Scalability+Testing+with+KWOK+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Revolutionizing Kube Scalability Testing with KWOK.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ub/revolutionizing-kube-scalability-testing-with-kwok-wei-huang-weiwei-yang-apple
- YouTube search: https://www.youtube.com/results?search_query=Revolutionizing+Kube+Scalability+Testing+with+KWOK+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3YH_2vqWAzQ
- YouTube title: Revolutionizing Kube Scalability Testing with KWOK - Wei Huang & Weiwei Yang, Apple
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/revolutionizing-kube-scalability-testing-with-kwok/3YH_2vqWAzQ.txt
- Transcript chars: 28152
- Keywords: control, cluster, testing, schedule, unicorn, running, objects, server, memory, basically, performance, controller, create, nothing, hollow, mentioned, another, actually

### Resumo baseado na transcript

first welcome everyone to join this today's session today we are going to talk about quar to see how we can use quar to do kubernetes scaling test Revolution firstly a little bit about ourselves my name is Wayan I work for Apple in the Apple service engineering team in the Upstream I'm the co-chair of six scheding I'm also the maintainer of some schedule plug of some Cal sub projects like schedule plugins and the qu uh my name is we way Yang I'm also from Apple uh working

### Excerpt da transcript

first welcome everyone to join this today's session today we are going to talk about quar to see how we can use quar to do kubernetes scaling test Revolution firstly a little bit about ourselves my name is Wayan I work for Apple in the Apple service engineering team in the Upstream I'm the co-chair of six scheding I'm also the maintainer of some schedule plug of some Cal sub projects like schedule plugins and the qu uh my name is we way Yang I'm also from Apple uh working in the AML data infrastructure and I'm ex vvp of apach unicorn um and also I love kubernetes and open source I worked on many many open source projects before so today's agenda is three parts first we will get you to know what's kuber ntic SC we test as what's current state and secondly we will see how we can use qu to solve the scarber test pit point point in a little different angle the lastly we will will show how in reality how cor helps unicorn to uh load the SC test the first part what is kubernetes scil test so it's the term scil test sounds a little scar you may be panic when you hear ter but by different definition is nothing but C how your components respond along with the number change of your kubernetes API objects so it can be multi-dimensional you can be can be nose change can be power change can be service change and points change PB PVC Etc and also can be a particular uh combination that you care most for for example for is maybe care most about how the end points end point size Etc how it works like or it's related uh through objects so why this is important because I think most of company right now are enter a day two world of running kubernetes so for day two it's a master to measure the component to be assure you know the limits and the boundary of your application running there and then so you can pre plan Your Capacity and so that you can control the cost and also your user know the limits so they can plan the application as well to know the limits and get the best user exp so in practice How We Do scri test in kubernetes context uh over simplified Paradigm is like this we should have the data inputs the data inputs is nothing but a series of uh work clows but you may not choose the raw Vina yice describe all the N all power Etc maybe you CH some tools help you abstract that with close and it also help you orchestrate you know t window like uh how you describe a scenario to deploy 5,000 nails and deploy uh 10K parts and see how how the C look looks like then in the
