---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["James Munnelly", "Andrea Tosatto", "Apple"]
sched_url: https://kccncna2022.sched.com/event/182HR/api-evolution-with-crds-best-practices-for-authoring-fuzz-testing-apis-james-munnelly-andrea-tosatto-apple
youtube_search_url: https://www.youtube.com/results?search_query=API+Evolution+With+CRDs%3A+Best+Practices+For+Authoring+%26+Fuzz+Testing+APIs+CNCF+KubeCon+2022
slides: []
status: parsed
---

# API Evolution With CRDs: Best Practices For Authoring & Fuzz Testing APIs - James Munnelly & Andrea Tosatto, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: James Munnelly, Andrea Tosatto, Apple
- Schedule: https://kccncna2022.sched.com/event/182HR/api-evolution-with-crds-best-practices-for-authoring-fuzz-testing-apis-james-munnelly-andrea-tosatto-apple
- Busca YouTube: https://www.youtube.com/results?search_query=API+Evolution+With+CRDs%3A+Best+Practices+For+Authoring+%26+Fuzz+Testing+APIs+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre API Evolution With CRDs: Best Practices For Authoring & Fuzz Testing APIs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182HR/api-evolution-with-crds-best-practices-for-authoring-fuzz-testing-apis-james-munnelly-andrea-tosatto-apple
- YouTube search: https://www.youtube.com/results?search_query=API+Evolution+With+CRDs%3A+Best+Practices+For+Authoring+%26+Fuzz+Testing+APIs+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Pn_1GvQvAyY
- YouTube title: API Evolution With CRDs: Best Practices For Authoring & Fuzz Test... James Munnelly & Andrea Tosatto
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/api-evolution-with-crds-best-practices-for-authoring-fuzz-testing-apis/Pn_1GvQvAyY.txt
- Transcript chars: 29321
- Keywords: actually, testing, resources, server, controller, conversion, schema, instance, resource, version, important, client, validation, behavior, another, operational, create, values

### Resumo baseado na transcript

cool um thanks very much for coming everyone um we're going to get started pretty promptly because we've got a lot of content to get through and uh everyone's got quite a schedule today I'm sure um so thank you for coming this is a talk on API Evolution with crds so um best practices for authoring crds fuzz testing all sorts and like how to maintain uh how to maintain your CDs so I'm James Munley I'm a field engineer at Apple um it kind of means I do

### Excerpt da transcript

cool um thanks very much for coming everyone um we're going to get started pretty promptly because we've got a lot of content to get through and uh everyone's got quite a schedule today I'm sure um so thank you for coming this is a talk on API Evolution with crds so um best practices for authoring crds fuzz testing all sorts and like how to maintain uh how to maintain your CDs so I'm James Munley I'm a field engineer at Apple um it kind of means I do all sorts and this is my colleague here hi hi hello everyone um and that was after work in essery at Apple as well uh with James we both work on the kubernetes platform at Apple and this talk is really like about like our journey like internally in like building ordering and and also like advising partner teams on how to extend API using series and the Germany with crd is actually like start really like with the authoring part right is it's like any API like when you get like to design it and implement it and think like how to do things the first challenge is really like about the modeling um in in the context of kubernetes there are a lot of examples right in the community the community is quite big uh at times too many it can be overwhelming like to find like the right information the best practices best practices something that to me is also quite funny is that often like when with Riker we used to look into the standard Library as a reference on best practices but kubernetes has been here very long and not always like the core resources are the best representation because there are some trade-off and the community evolve their understanding on the API so maybe not always the core resources are the right place to look at on how to implement things um and also like there are also other challenges related to the design of the crds right in do we model everything in one single resource do we use more and actually like kubernetes give us like this object ref uh field oops object field which help us like to backup crds but at the same time really increase the complexity of of controllers because now you need to start like handling into the code like this this references and as well create cognitive or over for the users but generally like one one best practice that we learn is that it's it's really worth like breaking down like the model into more uh resources itself and a good example if you think about it is like the certificate resource for instance like you have water source the 101 certificate or as well as
