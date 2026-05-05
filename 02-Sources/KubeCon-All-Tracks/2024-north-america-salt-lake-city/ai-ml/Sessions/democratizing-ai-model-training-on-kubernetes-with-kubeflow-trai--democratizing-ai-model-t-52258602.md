---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Andrey Velichkevich", "Apple", "Yuki Iwai", "CyberAgent", "Inc."]
sched_url: https://kccncna2024.sched.com/event/1i7nV/democratizing-ai-model-training-on-kubernetes-with-kubeflow-trainjob-and-jobset-andrey-velichkevich-apple-yuki-iwai-cyberagent-inc
youtube_search_url: https://www.youtube.com/results?search_query=Democratizing+AI+Model+Training+on+Kubernetes+with+Kubeflow+TrainJob+and+JobSet+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Democratizing AI Model Training on Kubernetes with Kubeflow TrainJob and JobSet - Andrey Velichkevich, Apple & Yuki Iwai, CyberAgent, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Andrey Velichkevich, Apple, Yuki Iwai, CyberAgent, Inc.
- Schedule: https://kccncna2024.sched.com/event/1i7nV/democratizing-ai-model-training-on-kubernetes-with-kubeflow-trainjob-and-jobset-andrey-velichkevich-apple-yuki-iwai-cyberagent-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Democratizing+AI+Model+Training+on+Kubernetes+with+Kubeflow+TrainJob+and+JobSet+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Democratizing AI Model Training on Kubernetes with Kubeflow TrainJob and JobSet.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nV/democratizing-ai-model-training-on-kubernetes-with-kubeflow-trainjob-and-jobset-andrey-velichkevich-apple-yuki-iwai-cyberagent-inc
- YouTube search: https://www.youtube.com/results?search_query=Democratizing+AI+Model+Training+on+Kubernetes+with+Kubeflow+TrainJob+and+JobSet+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Lgy4ir1AhYw
- YouTube title: Democratizing AI Model Training on Kubernetes with Kubeflow TrainJob and... A. Velichkevich, Y. Iwai
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/democratizing-ai-model-training-on-kubernetes-with-kubeflow-trainjob-a/Lgy4ir1AhYw.txt
- Transcript chars: 29414
- Keywords: training, actually, runtime, python, operator, parameters, support, configuration, distributed, scientist, learning, working, across, gpu, running, create, trainer, machine

### Resumo baseado na transcript

thank you for attending this session um I'm Uki working for cyber agent in Japan and so I'm technical read Q Pro utl and training working group and so I'm technically read um Cube kubernetes q and Ria for cube Contra manager jav API so today um my co-speaker Andre is unfortunately unable to attending this session in person so but so I got um videos from him so I will pra a video from him so let's start so today's session is so democratizing AI model training on cuberes

### Excerpt da transcript

thank you for attending this session um I'm Uki working for cyber agent in Japan and so I'm technical read Q Pro utl and training working group and so I'm technically read um Cube kubernetes q and Ria for cube Contra manager jav API so today um my co-speaker Andre is unfortunately unable to attending this session in person so but so I got um videos from him so I will pra a video from him so let's start so today's session is so democratizing AI model training on cuberes with c job and job set so the first part is um Android part so let me phase videos hey kcon I'm Andre I work at Apple I'm also member of the K steering committee I've been this committee for last six and a half years I've been involved in development of projects such as training operator and ctib and today before we actually going to share you how we going to democratize modal training on top of compus I want to speak a little bit about the background and history so let me first all talk about the data scientists so in Ideal World data scientists what they want they want to write their fighter code and want to have have a way to actually quickly scale it and the tricky part because it's actually interactive process they want to have a way to actually repeat this multiple times before to find like the best configuration for their model so they can push it to production but in reality there are many things which associated with this process for example you need to make sure you can appr properly configure your Docker images your data access maybe you want to like enable different policies like fail or success policies for full tolerance maybe you want to enable the gang scheduling or maybe you want to configure your uh resource cues for efficient uh Resource Management so we call all of this as kind of infrastructure pain which uh data scientists need to deal with before they can write the code and scale it and we need to find a way how we can abstract it and simplify it also there are many many challenges which which is associated with model training for example right now we live in the world of generative a models become very complex it has billions of parameters that is set also very huge so we need to find a way how we can distribute them across multiple GPU devices also we need to make sure like we efficiently manage the computer sources uh like gpus and tpus uh also like we need to find uh provide an API for all this diverse ml infrastructure and all this new distributor strategies like
