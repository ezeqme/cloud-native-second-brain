---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Multi-tenancy"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Michael Hrivnak", "Varsha Prasad Narsing", "Red Hat", "Rajula Vineet Reddy", "Francisco Borges Aurindo Barros", "CERN"]
sched_url: https://kccnceu2023.sched.com/event/1Hycm/operating-cern-saas-at-scale-with-operators-michael-hrivnak-varsha-prasad-narsing-red-hat-rajula-vineet-reddy-francisco-borges-aurindo-barros-cern
youtube_search_url: https://www.youtube.com/results?search_query=Operating+CERN+SaaS+at+Scale+with+Operators+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Operating CERN SaaS at Scale with Operators - Michael Hrivnak & Varsha Prasad Narsing, Red Hat; Rajula Vineet Reddy & Francisco Borges Aurindo Barros, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael Hrivnak, Varsha Prasad Narsing, Red Hat, Rajula Vineet Reddy, Francisco Borges Aurindo Barros, CERN
- Schedule: https://kccnceu2023.sched.com/event/1Hycm/operating-cern-saas-at-scale-with-operators-michael-hrivnak-varsha-prasad-narsing-red-hat-rajula-vineet-reddy-francisco-borges-aurindo-barros-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Operating+CERN+SaaS+at+Scale+with+Operators+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Operating CERN SaaS at Scale with Operators.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hycm/operating-cern-saas-at-scale-with-operators-michael-hrivnak-varsha-prasad-narsing-red-hat-rajula-vineet-reddy-francisco-borges-aurindo-barros-cern
- YouTube search: https://www.youtube.com/results?search_query=Operating+CERN+SaaS+at+Scale+with+Operators+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0sBgS_3xT8U
- YouTube title: Operating CERN SaaS at Scale with Operators
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/operating-cern-saas-at-scale-with-operators/0sBgS_3xT8U.txt
- Transcript chars: 33010
- Keywords: operator, basically, version, metrics, actually, status, cluster, controller, operators, create, resource, custom, specific, having, software, around, websites, available

### Resumo baseado na transcript

welcome everyone thank you for joining us come on in there are some uh there's some additional empty seats well a few of them although they're going are these reserved for somebody are they for us allegedly what does that say there's a few more seats if you wander up this direction is good okay that we got reserved there's one here we got a lot of friendly people here at kubecon so make some friends we've got uh empty seats there maybe raise your hand if you got an

### Excerpt da transcript

welcome everyone thank you for joining us come on in there are some uh there's some additional empty seats well a few of them although they're going are these reserved for somebody are they for us allegedly what does that say there's a few more seats if you wander up this direction is good okay that we got reserved there's one here we got a lot of friendly people here at kubecon so make some friends we've got uh empty seats there maybe raise your hand if you got an empty seat next to you uh and you're and you're interested to meet a new Cube Connor well we got tons of them up here come on in make room uh we're going to talk about CERN and what they've done with the operator framework to make their lives easier um I am Michael from Red Hat this is varsha we're operator framework contributors and maintainers over various times we also have here with us Francisco and rajula they're sres at CERN and we're going to talk about how we came together their operator they created caught our eye so they're going to introduce what they've done we'll discuss a bit amongst ourselves some observations about what they've done their experience we'll have some discussion over here and then invite you to ask your questions and join in that discussion uh in the latter portion of this so thank you again for coming and uh rajula please take it away [Applause] it's just a great bit of introverty so we're the center for European nuclear research uh we are the world's largest and the biggest particle accelerator uh this is a one of the accelerators where we Collide subatomic particles this is called Atlas just to give a bit of Glimpse this weighs among 7000 tons which is equal to the weight of the Eiffel Tower and this is uh the collider so it's a let's see uh it's around 27 kilometers in diameter and you see the Geneva Lake and the Swiss apps in the background and it's not just physics what we do so CERN is also a place where the worldwide pad was invented and we actually do a bit more than just that so we have a lot of member states from around the world and the main source of collaboration and communication happens through websites so we host a lot of websites so we specifically come from the team where we host publicly available websites like home.7 and atlas.cern so just a quick glimpse of our infrastructure so we manage content Management Systems basically it's Drupal instances so the users basically can create update and delete without a lot of technical knowledge and we wan
