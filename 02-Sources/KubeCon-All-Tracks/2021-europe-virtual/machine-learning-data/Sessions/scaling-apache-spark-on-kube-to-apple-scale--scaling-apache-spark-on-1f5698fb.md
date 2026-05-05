---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Amanda Moran", "Holden Karau", "Apple"]
sched_url: https://kccnceu2021.sched.com/event/iE28/scaling-apache-spark-on-kube-to-apple-scale-amanda-moran-holden-karau-apple
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Apache+Spark+on+Kube+to+Apple+Scale+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Scaling Apache Spark on Kube to Apple Scale - Amanda Moran & Holden Karau, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Amanda Moran, Holden Karau, Apple
- Schedule: https://kccnceu2021.sched.com/event/iE28/scaling-apache-spark-on-kube-to-apple-scale-amanda-moran-holden-karau-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Apache+Spark+on+Kube+to+Apple+Scale+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Scaling Apache Spark on Kube to Apple Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE28/scaling-apache-spark-on-kube-to-apple-scale-amanda-moran-holden-karau-apple
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Apache+Spark+on+Kube+to+Apple+Scale+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xX2z8ndp_zg
- YouTube title: Scaling Apache Spark on Kube to Apple Scale - Amanda Moran & Holden Karau, Apple
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/scaling-apache-spark-on-kube-to-apple-scale/xX2z8ndp_zg.txt
- Transcript chars: 26772
- Keywords: actually, cluster, resource, python, dynamic, little, workloads, better, executor, apache, allows, storage, essentially, executors, another, allocation, important, resources

### Resumo baseado na transcript

hi there all welcome and thank you so much for joining us we're going to be talking about scaling apache spark on kubernetes we're amanda and holden and we're so delighted to be here at kubecon eu so first and foremost we're going to tell you a little bit about ourselves then we're going to talk about what is apache spark and why it matters to kubernetes what is yarn and mesos spark standalone mode so get ready for that one why you should put spark on kubernetes what worked

### Excerpt da transcript

hi there all welcome and thank you so much for joining us we're going to be talking about scaling apache spark on kubernetes we're amanda and holden and we're so delighted to be here at kubecon eu so first and foremost we're going to tell you a little bit about ourselves then we're going to talk about what is apache spark and why it matters to kubernetes what is yarn and mesos spark standalone mode so get ready for that one why you should put spark on kubernetes what worked well while we worked through this process and what didn't work as good best practices for doing this kind of transformation new features that have been implemented and upstreamed and areas for improvement so who are we so you'll see two two of us uh in this picture and this collection of pictures work for apple and that is me and holden and you also see our two pups timber and jack they support us throughout the day as we get our work done both of us have been and have worked for apple uh for over a year i think holden is it's getting close to two years and um both of us have been um a part of the apache spark community holden much more so she's an apache committer she's written books on apache spark she's been with it pretty much from the get-go i came to spark a little bit later but i've been involved with it for quite a few years i've done quite a few talks on spark and and it's a it's a technology that um i enjoy i like teaching other people about and using myself so all right so let's talk about spark and what are these things so what is spark so a lightning fast unified analytics engine is one of the taglines you'll hear quite frequently but apache spark is really used to do large-scale data processing on large data sets it's used by data scientists data engineers machine learning engineers basically anyone who is working with large data sets basically regardless of title so apache spark allows for batch jobs streaming jobs the ability to use spark sql r python scala or java you can do machine learning using spark and you can also do graph analytics with spark as well so some other taglines you may have heard about spark which is it's map hadoop mapreduce uh but with seven cups of coffee um of course we have a little disclaimer there you know check with your hardware vendor first but i mean there has been i mean there's been so many numbers thrown around the years uh but essentially you know spark jobs because of their ability to utilize uh memory and large uh and do that large pr
