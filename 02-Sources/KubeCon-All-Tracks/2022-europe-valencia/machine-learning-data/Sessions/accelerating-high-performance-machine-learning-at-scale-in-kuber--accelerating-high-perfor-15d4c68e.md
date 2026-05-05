---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Alejandro Saucedo", "The Institute for Ethical AI", "Machine Learning", "Elena Neroslavskaya", "Microsoft"]
sched_url: https://kccnceu2022.sched.com/event/ytn3/accelerating-high-performance-machine-learning-at-scale-in-kubernetes-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning-elena-neroslavskaya-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Accelerating+High-Performance+Machine+Learning+at+Scale+in+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Accelerating High-Performance Machine Learning at Scale in Kubernetes - Alejandro Saucedo, The Institute for Ethical AI & Machine Learning & Elena Neroslavskaya, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Alejandro Saucedo, The Institute for Ethical AI, Machine Learning, Elena Neroslavskaya, Microsoft
- Schedule: https://kccnceu2022.sched.com/event/ytn3/accelerating-high-performance-machine-learning-at-scale-in-kubernetes-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning-elena-neroslavskaya-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Accelerating+High-Performance+Machine+Learning+at+Scale+in+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Accelerating High-Performance Machine Learning at Scale in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytn3/accelerating-high-performance-machine-learning-at-scale-in-kubernetes-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning-elena-neroslavskaya-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Accelerating+High-Performance+Machine+Learning+at+Scale+in+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hj_lozIqo5M
- YouTube title: Accelerating High-Performance Machine Learning at Scale i... Alejandro Saucedo & Elena Neroslavskaya
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/accelerating-high-performance-machine-learning-at-scale-in-kubernetes/hj_lozIqo5M.txt
- Transcript chars: 33088
- Keywords: actually, learning, machine, server, models, cluster, runtime, seldom, gpu, basically, running, python, deployment, deploy, githubs, inference, pushing, production

### Resumo baseado na transcript

all right so uh thank you everybody for coming today uh we have a very exciting and interesting topic uh today we're going to be diving into the topic of accelerating high performance machine learning at scale in kubernetes so a little bit about myself and my co-speaker my name is alejandro saucedo i am engineering director at zelda technologies a machine learning deployment and monitoring startup based in london i'm also chief scientist at the institute for ethical ai and governing member council at large at the acm my

### Excerpt da transcript

all right so uh thank you everybody for coming today uh we have a very exciting and interesting topic uh today we're going to be diving into the topic of accelerating high performance machine learning at scale in kubernetes so a little bit about myself and my co-speaker my name is alejandro saucedo i am engineering director at zelda technologies a machine learning deployment and monitoring startup based in london i'm also chief scientist at the institute for ethical ai and governing member council at large at the acm my co-speaker couldn't make it today she's still based in vancouver but she was able to send us some exciting videos of the demos that you will be able to try out yourselves with the jupiter notebooks and deploy on your own site so elena is a senior cloud architect at microsoft and today we're going to be able to show you a great interesting collaboration uh productionizing machine learning uh you know at what is scale we're going to be taking a use case which in this case is going to be a text generation um you know exciting uh gpt2 model we're going to be showcasing how to perform optimizations on machine learning of course this is a kubernetes conference not a machine learning conference so we're going to be actually covering more about the steps productionizing those models some of the nuances of how these practicalities change when you're dealing with machine learning as opposed to just normal software and then how we're going to be deploying and scaling this in a kubernetes cluster finally we're going to be covering some cloud native best practices things like githubs and operational monitoring that you would introduce in normal microservices but adapting that into the machine learning space so let's get started let's start with the what so we're going to be taking this machine learning use case that some of you may have come across before so this is the gpd2 text generation use case what it basically does is it takes a text input and it simply generates the next token right and what this allows you to do is to basically generate human-like um you know uh text right so here you can see that the input is the tokens a robot may you can see that the model actually generates that next token so that's basically what we're going to be doing the reason why we're taking this use case is for a couple of uh various uh perspectives the first one is that it's quite intuitive you can see some of the exciting value not just in how it actually performs
