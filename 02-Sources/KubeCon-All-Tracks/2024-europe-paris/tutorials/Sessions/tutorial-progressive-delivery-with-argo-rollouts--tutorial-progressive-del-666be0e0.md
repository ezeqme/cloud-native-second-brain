---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Tutorials"
themes: ["GitOps Delivery"]
speakers: ["Kevin Dubois", "Harriet Lawrence", "Natale Vinto", "Red Hat", "Christian Hernandez", "Akuity", "Kostis Kapelonis", "Codefresh"]
sched_url: https://kccnceu2024.sched.com/event/1YeSd/tutorial-progressive-delivery-with-argo-rollouts-kevin-dubois-harriet-lawrence-natale-vinto-red-hat-christian-hernandez-akuity-kostis-kapelonis-codefresh
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Progressive+Delivery+with+Argo+Rollouts+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Progressive Delivery with Argo Rollouts - Kevin Dubois, Harriet Lawrence & Natale Vinto, Red Hat; Christian Hernandez, Akuity; Kostis Kapelonis, Codefresh

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Tutorials]]
- Temas: [[GitOps Delivery]]
- País/cidade: France / Paris
- Speakers: Kevin Dubois, Harriet Lawrence, Natale Vinto, Red Hat, Christian Hernandez, Akuity, Kostis Kapelonis, Codefresh
- Schedule: https://kccnceu2024.sched.com/event/1YeSd/tutorial-progressive-delivery-with-argo-rollouts-kevin-dubois-harriet-lawrence-natale-vinto-red-hat-christian-hernandez-akuity-kostis-kapelonis-codefresh
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Progressive+Delivery+with+Argo+Rollouts+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Progressive Delivery with Argo Rollouts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSd/tutorial-progressive-delivery-with-argo-rollouts-kevin-dubois-harriet-lawrence-natale-vinto-red-hat-christian-hernandez-akuity-kostis-kapelonis-codefresh
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Progressive+Delivery+with+Argo+Rollouts+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tnB0TwEqNFA
- YouTube title: Tutorial: Progressive Delivery with Argo Rollouts
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-progressive-delivery-with-argo-rollouts/tnB0TwEqNFA.txt
- Transcript chars: 26769
- Keywords: little, argo, version, delivery, course, production, rollouts, progressive, release, basically, everything, actually, metrics, cluster, rolling, deploy, canary, access

### Resumo baseado na transcript

all right he made it until Friday afternoon I'm impressed bra all right so uh we're going to do a a Hands-On tutorial this afternoon on uh hand on Argo rollouts so we're going to do a progressive delivery of our application and um yeah you'll see if uh well we'll see if it works first of all because we've never done a Hands-On lab for so many people um but we're reasonably confident so we'll see anyways uh so I'm Kevin du I'm a developer Advocate at red hat it's up to you read through the tutorial and uh try out the different steps in the meantime I'll do a a quick little demo of uh what we'll eventually see so here we have um an application if you go to the Argo rollouts

### Excerpt da transcript

all right he made it until Friday afternoon I'm impressed bra all right so uh we're going to do a a Hands-On tutorial this afternoon on uh hand on Argo rollouts so we're going to do a progressive delivery of our application and um yeah you'll see if uh well we'll see if it works first of all because we've never done a Hands-On lab for so many people um but we're reasonably confident so we'll see anyways uh so I'm Kevin du I'm a developer Advocate at red hat and with me is natal he's uh he's my manager so make sure yeah any complaints don't tell him no uh and then we have uh Christian uh who's from acuti then we have Harriet also from Red house so we have three people from Red Hat here and then uh we also have uh ctis from uh from code fresh and uh well everybody here Works a little bit on Argo C some or Argo the Argo project some little more uh like Christian and kosis are are maintainers and then some of them a little less like me and so that's why I'm doing a presentation because I know the least about it all right so um this is this is how I started with with uh Progressive delivery so I don't know if you uh recognize this you know so filezilla but anyway with the fdp right you know like copy paste or in the CLI maybe if you were a little more advanced already um yeah that wasn't really a very sustainable way right and uh we had many times that in the middle of the night we'd have to uh get up and and support any kind of issues because it was very unpredictable and then uh of course we evolved right so cicd basically for most of us uh meant Jenkins right so we built uh some Advanced pipelines and then maybe some automated delivery too but yeah it's it's still a little bit uh finicky with Jenkins it's not necessarily Built For The Continuous delivery right it's more a CI tool and um we evolved right we evolved from this uh more monolithic kind of applications where we have one thing that needs to go to production and it was still okay to do you know a more Hands-On approach to delivering our software but then once we went into more distributed architectures you know that means more and more delivery pipelines right you see those little tubes those present kind of pipelines and uh we needed better ways of course so uh you can see you know our developer flow has M has kind of evolved over the years right and so now we have this inter Loop where we're doing our local development and we're do we're doing our building and our testing and debugging and uh mayb
