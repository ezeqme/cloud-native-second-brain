---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Erik Jacobs", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182Fk/computational-fluid-dynamics-cfd-analysis-with-kubernetes-kubeflow-and-openfoam-erik-jacobs-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Computational+Fluid+Dynamics+%28CFD%29+Analysis+With+Kubernetes%2C+Kubeflow%2C+And+OpenFOAM+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Computational Fluid Dynamics (CFD) Analysis With Kubernetes, Kubeflow, And OpenFOAM - Erik Jacobs, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Erik Jacobs, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182Fk/computational-fluid-dynamics-cfd-analysis-with-kubernetes-kubeflow-and-openfoam-erik-jacobs-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Computational+Fluid+Dynamics+%28CFD%29+Analysis+With+Kubernetes%2C+Kubeflow%2C+And+OpenFOAM+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Computational Fluid Dynamics (CFD) Analysis With Kubernetes, Kubeflow, And OpenFOAM.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fk/computational-fluid-dynamics-cfd-analysis-with-kubernetes-kubeflow-and-openfoam-erik-jacobs-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Computational+Fluid+Dynamics+%28CFD%29+Analysis+With+Kubernetes%2C+Kubeflow%2C+And+OpenFOAM+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wKpBip1217c
- YouTube title: Computational Fluid Dynamics (CFD) Analysis With Kubernetes, Kubeflow, And OpenFOAM - Erik Jacobs
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/computational-fluid-dynamics-cfd-analysis-with-kubernetes-kubeflow-and/wKpBip1217c.txt
- Transcript chars: 33274
- Keywords: storage, launcher, actually, container, operator, probably, workers, whatever, experiment, little, dynamics, trying, picture, deeper, anyway, communication, network, wanted

### Resumo baseado na transcript

uh good morning everybody thanks for showing up today this is uh computational fluid dynamics kubernetes uh Cube flow open philam um before we get started I just wanted to thank two folks uh I don't think either of them are in the room today Eduardo orango and Aldo go kodor um they were super helpful when I was going through this sort of process of figuring all this stuff out um Eduardo's actually not at Red Hat anymore he moved over to Nvidia so um either way still helpful

### Excerpt da transcript

uh good morning everybody thanks for showing up today this is uh computational fluid dynamics kubernetes uh Cube flow open philam um before we get started I just wanted to thank two folks uh I don't think either of them are in the room today Eduardo orango and Aldo go kodor um they were super helpful when I was going through this sort of process of figuring all this stuff out um Eduardo's actually not at Red Hat anymore he moved over to Nvidia so um either way still helpful or thankful for his help um this is not a super serious presentation it's Friday we've been here all week it's you know all tired um it's going to be fun I promise I hope uh if you want serious there's a blog post that I wrote that details all the Gory GitHub repos and all this other stuff this presentation's on the sked website you don't have to worry we can go back to this whatever um so if you don't get a picture of this it's fine um and like I said this is going to be fun full bad jokes terrible memes all that kind of stuff so I'm getting at least one round of applause so we're good okay here we go this presentation's built like building blocks right we're just going to try to put things together get deeper deeper deeper as we go to explain how I actually was able to achieve this because in reality it was mostly just kind of an experiment um before we get started just a couple questions if you're kubernetes user raise your hand real quick everybody okay that's not totally a surprise who's doing HPC not necessarily on kubernetes just anything that would qualifies as HPC only a few anybody doing MPI stuff about the same number and then lastly open foam existing one one okay cool uh how did we get here so me uh I've been a red hat for 14 and 1 12 years I'm not a software engineer I'm not a kubernetes cube flow open foam developer um I'm not an aerodynamicist but I do have a race car and it does have a wing on it so uh I ended up getting this email from an account team out of APAC and they were like oh this automaker is doing open foam in a container they want to do it in VMS and I was like can we do this on kubernetes and I remembered I have these friends who do aerodynamic stuff and they offered me some of their um uh models to play with and I was like cool okay let's let's let's do an experiment right let me see if I can run their fluid dynamics Wing job in kubernetes environment so review open foam and MPI what is MPI it does parallel or distributed computing so we have lots of thin
