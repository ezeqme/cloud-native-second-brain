---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Open Interfaces + Interoperability"
themes: ["AI ML"]
speakers: ["Cici Huang", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyXw/the-path-to-self-contained-crds-cici-huang-google
youtube_search_url: https://www.youtube.com/results?search_query=The+Path+to+Self+Contained+CRDs+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Path to Self Contained CRDs - Cici Huang, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Cici Huang, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyXw/the-path-to-self-contained-crds-cici-huang-google
- Busca YouTube: https://www.youtube.com/results?search_query=The+Path+to+Self+Contained+CRDs+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Path to Self Contained CRDs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXw/the-path-to-self-contained-crds-cici-huang-google
- YouTube search: https://www.youtube.com/results?search_query=The+Path+to+Self+Contained+CRDs+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KIL1BAq3J2g
- YouTube title: The Path to Self Contained CRDs - Cici Huang, Google
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-path-to-self-contained-crds/KIL1BAq3J2g.txt
- Transcript chars: 24088
- Keywords: policy, validation, resources, cluster, support, couple, validations, version, conversion, resource, write, called, already, customer, request, expression, basically, pretty

### Resumo baseado na transcript

um first a little bit about myself my name is CeCe Huang and I'm currently working at Google as a senior software engineer I just reached my three years of contributing to kubernetes community I initially started in Sega cloud provider and I've been the kubernetes contributor award I think that year on 2020 and then I shifted to say API Machinery I'm currently a contributor to ckpair Machinery with focus of the extensible features and additionally I have served as the release leader for the kubernetes 125 and I away but unfortunately it's not what's happening with crds for quite some time you just can't write all the validations you want with your security and since your controller doesn't support you just have to wait until controller break and report an error somewhere and has already um having a working implementation for this which we're really excited about and we hope we could bring it to kubernetes and here is a draft cap for supporting crd conversion with cell similarly as crd validation rules we just talked about it's

### Excerpt da transcript

um first a little bit about myself my name is CeCe Huang and I'm currently working at Google as a senior software engineer I just reached my three years of contributing to kubernetes community I initially started in Sega cloud provider and I've been the kubernetes contributor award I think that year on 2020 and then I shifted to say API Machinery I'm currently a contributor to ckpair Machinery with focus of the extensible features and additionally I have served as the release leader for the kubernetes 125 and I was the release manager for the past 127 release which we just released yet last week so today I'm going to talk about the customer resource definitions and the effort we did to make it more self-contained we got a bunch to cover today I'll begin with like reviewing the Journey of crd in the past and then talk a little bit about the common expression language which also known as cell and then talk about like how we Leverage The Power of cell and make crd even more self-contained and also I will talk about the other areas we were able to expand the power on things like policy enforcement area and I'll leave a couple minutes for QA in the end let's get it started then the Journey of crd so in the very early stage in kubernetes we have realized that keep adding the building apis is not going to be a long-standing solution for variety of usage that's when customer resource definition comes into picture and it initially known as the third party resource and has been in stable since uh 1 16.

so it allows users to extend and customize the kubernetes API with their own resources and it still remains one of the most important extension mechanisms inside kubernetes so many core Community functions are now built using customer resources and it makes kubernetes more modular so in the past we have made a lot of effort to try to make charity as good as building types so we added a versioning support added sub resources we added open API scheme structure schema and many other features but along the way there is a topic continuously being brought up the validation so why are validation so critical I guess the answer aligns in the fact that if you don't validate the data comes into your system later things going to break in a way that is hard to reason and debug at that point is going to be much more difficult excuse me so it is important to tell developers what they did wrong at the time when the request is submitted and give them the chance to fix it right away b
