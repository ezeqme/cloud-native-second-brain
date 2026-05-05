---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Christopher Hanson", "RX-M", "llc."]
sched_url: https://kccnceu2021.sched.com/event/iE3v/choose-wisely-understanding-kubernetes-selectors-christopher-hanson-rx-mllc
youtube_search_url: https://www.youtube.com/results?search_query=Choose+Wisely%3A+Understanding+Kubernetes+Selectors+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Choose Wisely: Understanding Kubernetes Selectors - Christopher Hanson, RX-M,llc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Christopher Hanson, RX-M, llc.
- Schedule: https://kccnceu2021.sched.com/event/iE3v/choose-wisely-understanding-kubernetes-selectors-christopher-hanson-rx-mllc
- Busca YouTube: https://www.youtube.com/results?search_query=Choose+Wisely%3A+Understanding+Kubernetes+Selectors+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Choose Wisely: Understanding Kubernetes Selectors.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3v/choose-wisely-understanding-kubernetes-selectors-christopher-hanson-rx-mllc
- YouTube search: https://www.youtube.com/results?search_query=Choose+Wisely%3A+Understanding+Kubernetes+Selectors+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dLe0TZEGhxo
- YouTube title: Choose Wisely: Understanding Kubernetes Selectors - Christopher Hanson, RX-M,llc.
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/choose-wisely-understanding-kubernetes-selectors/dLe0TZEGhxo.txt
- Transcript chars: 26080
- Keywords: deployment, controller, labels, replica, course, selector, canary, controllers, create, standalone, production, actually, command, update, deployments, deploy, selectors, delete

### Resumo baseado na transcript

hello and welcome to choose wisely understanding kubernetes selectors my name is chris and i'll be taking you through this session uh i work for a company called rxm we are a cloud native training and consulting firm so i do a lot of training i do some consulting and i do a lot of speaking so you may have seen me last year at uh kubecon here in europe well i suppose it was virtual because of co-ed and talked about uh roll outs and roll backs and behaviors

### Excerpt da transcript

hello and welcome to choose wisely understanding kubernetes selectors my name is chris and i'll be taking you through this session uh i work for a company called rxm we are a cloud native training and consulting firm so i do a lot of training i do some consulting and i do a lot of speaking so you may have seen me last year at uh kubecon here in europe well i suppose it was virtual because of co-ed and talked about uh roll outs and roll backs and behaviors with controllers today it's sort of related in that we're going to talk about controller behavior with selectors so without further ado let's get started so before we talk about how controllers use selectors we need to talk about what they're selecting right so in a kubernetes cluster most objects have some sort of label and they may even have some sort of annotation and this could be any object a pod a node service the nice thing about labels is that they're selectable right and so uh we can actually use kubectl commands to create labels uh review labels so as you can see on the slide we've got the show labels flag we can add a label after the fact so if an object already exists we can use the label command to add additional labels we can overwrite existing labels if we want a new value for a particular key and we can remove them as well for existing objects in terms of using patterns to select things there's three patterns here there's the quality based which means that objects returned by that query have satisfied all the constraints uh they may have additional labels so if you just selected one label but there are several others the the object would still get returned by the cube ctl command as we see here they're set based so you may want to filter based on a key with several values and you want to see the objects that have um one or more values and then the key name uh you can just use the key and and see all the values for a particular uh key value pair and so you can see some patterns here we've got the team key and we're using in scarif with bespin and we're separating the two values with a comma and that logically ends and so we get uh all of the results back for the objects that have both team equal scarif and team equal specimen we can expand upon that by using a set base selector and an equality-based selector so a second example here is team in scarif best been with apical's rideshare and then of course that minimizes the results that get returned we can even use labels with things like the
