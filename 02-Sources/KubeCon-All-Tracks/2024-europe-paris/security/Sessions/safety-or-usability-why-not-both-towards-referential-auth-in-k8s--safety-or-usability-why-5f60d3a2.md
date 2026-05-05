---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security"]
speakers: ["Rob Scott", "Google", "Mo Khan", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1YeMO/safety-or-usability-why-not-both-towards-referential-auth-in-k8s-rob-scott-google-mo-khan-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Safety+or+Usability%3A+Why+Not+Both%3F+Towards+Referential+Auth+in+K8s+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Safety or Usability: Why Not Both? Towards Referential Auth in K8s - Rob Scott, Google & Mo Khan, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Rob Scott, Google, Mo Khan, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1YeMO/safety-or-usability-why-not-both-towards-referential-auth-in-k8s-rob-scott-google-mo-khan-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Safety+or+Usability%3A+Why+Not+Both%3F+Towards+Referential+Auth+in+K8s+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Safety or Usability: Why Not Both? Towards Referential Auth in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMO/safety-or-usability-why-not-both-towards-referential-auth-in-k8s-rob-scott-google-mo-khan-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Safety+or+Usability%3A+Why+Not+Both%3F+Towards+Referential+Auth+in+K8s+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HLWXuV3vJRg
- YouTube title: Safety or Usability: Why Not Both? Towards Referential Auth in K8s - Rob Scott, Google & Mo Khan
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/safety-or-usability-why-not-both-towards-referential-auth-in-k8s/HLWXuV3vJRg.txt
- Transcript chars: 29061
- Keywords: reference, access, controller, gateway, ingress, actually, secrets, controllers, namespace, authorization, references, purpose, secret, author, pattern, concept, account, authorizer

### Resumo baseado na transcript

thank you everyone for coming my name is Rob Scott I work at Google on GK networking and today we're going to be talking about referential authorization and what it might look like in kubernetes uh this is particularly relevant to me because I've spent a lot of time thinking about Ingress and Gateway API and how unfortunately insecure many of the implementations of those apis are uh and hopefully this can help hey everyone I'm Mo uh I work at Microsoft uh so this talk really appeals to me

### Excerpt da transcript

thank you everyone for coming my name is Rob Scott I work at Google on GK networking and today we're going to be talking about referential authorization and what it might look like in kubernetes uh this is particularly relevant to me because I've spent a lot of time thinking about Ingress and Gateway API and how unfortunately insecure many of the implementations of those apis are uh and hopefully this can help hey everyone I'm Mo uh I work at Microsoft uh so this talk really appeals to me because it intersects uh multiple Community roles that I hold uh so I'm a seot lead as well as a member of the kubernetes security response committee uh so yeah I'm really looking forward to having this stuff uh so Secrets uh so I like to keep my secrets to myself and I hope you do as well and unfortunately that's not always the case in kubernetes uh so in particular if you run Ingress controllers today uh you give them access to all Secrets uh whether you thought about it or not but this is not a good thing right um it's actually a really bad State the isolation between like the data plane and control plane of most Ingress controllers is actually pretty weak and when I say control plane I mean like the go code that is your kubernetes controller and your data plane is the actual raw like C code that's running your networking stuff right and as you can imagine when you put these things close to each other in ways that that aren't necessarily what they were designed to do well you get cves um so I'm going to pick on the Ingress engine X for a little bit here and you know when you talk about cves you want to pick you want to find the like the really good ones right like or the really bad ones that are high severity so the you know we've had seven so far and I was like okay I'll pick the worst one oh I'm sorry they were all high so they're all bad um so we'll just we'll pick my favorite one because it's just funny um so did you know that you can embed Lua in your Ingress config and have engine X process it for you and you know what could go wrong it's amazing uh so like what if I had some Lua that wanted to read a file on disk and maybe I wanted to put the contents of that file into a variable and then maybe I wanted to have an endpoint on my Ingress that just you know output that that nice little variable you know and so now if I can make an Ingress I can just I don't know Echo out that service account controller token that by the way you decided to grant full read access to
