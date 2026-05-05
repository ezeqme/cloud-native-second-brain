---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Serverless"
themes: ["Serverless"]
speakers: ["Ricardo Zanini Fernandes", "Red Hat"]
sched_url: https://kccnceu2022.sched.com/event/ytln/create-your-first-cncf-serverless-workflow-project-with-kogito-and-knative-ricardo-zanini-fernandes-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Create+Your+First+CNCF+Serverless+Workflow+Project+with+Kogito+and+Knative+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Create Your First CNCF Serverless Workflow Project with Kogito and Knative - Ricardo Zanini Fernandes, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Serverless]]
- Temas: [[Serverless]]
- País/cidade: Spain / Valencia
- Speakers: Ricardo Zanini Fernandes, Red Hat
- Schedule: https://kccnceu2022.sched.com/event/ytln/create-your-first-cncf-serverless-workflow-project-with-kogito-and-knative-ricardo-zanini-fernandes-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Create+Your+First+CNCF+Serverless+Workflow+Project+with+Kogito+and+Knative+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Create Your First CNCF Serverless Workflow Project with Kogito and Knative.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytln/create-your-first-cncf-serverless-workflow-project-with-kogito-and-knative-ricardo-zanini-fernandes-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Create+Your+First+CNCF+Serverless+Workflow+Project+with+Kogito+and+Knative+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yl6vK6TFRk4
- YouTube title: Create Your First CNCF Serverless Workflow Project with Kogito and Kna... Ricardo Zanini Fernandes
- Match score: 0.932
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/create-your-first-cncf-serverless-workflow-project-with-kogito-and-kna/yl6vK6TFRk4.txt
- Transcript chars: 27190
- Keywords: workflow, subscription, application, technology, create, specification, workflows, whatever, describe, events, within, itself, execution, platform, please, working, course, functions

### Resumo baseado na transcript

welcome many thanks guys for being here uh it's nice to see a lot of people interested in workflows in general uh my name is ricardo zanini um at red hat i'm principal software engineer and today we're going to talk about uh workflows and uh basically two projects that i'm involved in the community the first one the cncf service workflow specification um our implementation red hat what we're doing for that spec and a little bit of demonstrations use cases and as promised in the description of this

### Excerpt da transcript

welcome many thanks guys for being here uh it's nice to see a lot of people interested in workflows in general uh my name is ricardo zanini um at red hat i'm principal software engineer and today we're going to talk about uh workflows and uh basically two projects that i'm involved in the community the first one the cncf service workflow specification um our implementation red hat what we're doing for that spec and a little bit of demonstrations use cases and as promised in the description of this talk by the end hopefully you guys will be met will be uh able to create your own workflow project using this technology right okay uh first thing about the spec itself um this is a cncf sandbox project for quite some time we're working towards incubation right now uh it is a a dsl to describe workflows so we are working through this um to be a vendor neutral specification to describe workflow so uh any kind of technology or implementation on projects out there being you know open source or not can use this pack you know all the the workflows descriptors um the parts of the specification to do the all the implementation in your site i'm going to talk about a little bit more about that uh being a spec on cncf you know open source we are focusing on standards so everything that we do everything that we connect uh or um are supposed to have a standard so it is like uh open api jrpc all those kinds of things all those kind of things it is uh related to the spec as well i'm gonna explain that a little bit more uh and of course there's a lot of projects and companies already helping us there in the in the in this back side and we are of course working looking for contributors so if you're interested in workflows or if your company is somewhat interested in workflow it would be nice to have you there you know to share your ideas or maybe taking a look in this pack and see if that fits your use case or not if it is not we can talk and you can change some things everything is you know uh open to talk so it is a very well welcome and warm community so go there and if you scan the qr code you're going to the surveillance workflow.io there's all the information is there we also have um a slack channel at the cncf like so you go for servlets workflow and we have a channel there we can connect and talk and you can ping me offline if you want uh okay let's talk about a bit a bit more about the specification itself um so it is based on standards like i said uh the first thing is
