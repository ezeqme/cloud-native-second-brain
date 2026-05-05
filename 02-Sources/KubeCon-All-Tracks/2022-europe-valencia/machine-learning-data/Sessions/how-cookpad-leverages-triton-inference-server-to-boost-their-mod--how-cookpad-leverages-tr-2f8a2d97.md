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
themes: ["AI ML", "Storage Data"]
speakers: ["Jose Navarro", "Prayana Galih", "Cookpad"]
sched_url: https://kccnceu2022.sched.com/event/ytmT/how-cookpad-leverages-triton-inference-server-to-boost-their-model-serving-jose-navarro-prayana-galih-cookpad
youtube_search_url: https://www.youtube.com/results?search_query=How+Cookpad+Leverages+Triton+Inference+Server+To+Boost+Their+Model+Serving+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How Cookpad Leverages Triton Inference Server To Boost Their Model Serving - Jose Navarro & Prayana Galih, Cookpad

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Spain / Valencia
- Speakers: Jose Navarro, Prayana Galih, Cookpad
- Schedule: https://kccnceu2022.sched.com/event/ytmT/how-cookpad-leverages-triton-inference-server-to-boost-their-model-serving-jose-navarro-prayana-galih-cookpad
- Busca YouTube: https://www.youtube.com/results?search_query=How+Cookpad+Leverages+Triton+Inference+Server+To+Boost+Their+Model+Serving+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How Cookpad Leverages Triton Inference Server To Boost Their Model Serving.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytmT/how-cookpad-leverages-triton-inference-server-to-boost-their-model-serving-jose-navarro-prayana-galih-cookpad
- YouTube search: https://www.youtube.com/results?search_query=How+Cookpad+Leverages+Triton+Inference+Server+To+Boost+Their+Model+Serving+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YMtLI1Ub85s
- YouTube title: How Cookpad Leverages Triton Inference Server To Boost Their Model S... Jose Navarro & Prayana Galih
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-cookpad-leverages-triton-inference-server-to-boost-their-model-ser/YMtLI1Ub85s.txt
- Transcript chars: 21457
- Keywords: gpu, triton, deploy, inference, models, multiple, cost, deployment, server, feature, tensorflow, tensor, machine, learning, platform, requests, performance, experience

### Resumo baseado na transcript

my name is jose navarro and this is praiana galif and we both are the machine learning platform team at cookbot today we are going to talk to you about how nvidia triton inference server can help you optimize three areas of your inference engine performance user experience for your machine learning teams and cost but first let me introduce you to cookpad a little bit for context cookpot is the largest online community for home cooking lovers we are making everyday cooking fun but why well the act of

### Excerpt da transcript

my name is jose navarro and this is praiana galif and we both are the machine learning platform team at cookbot today we are going to talk to you about how nvidia triton inference server can help you optimize three areas of your inference engine performance user experience for your machine learning teams and cost but first let me introduce you to cookpad a little bit for context cookpot is the largest online community for home cooking lovers we are making everyday cooking fun but why well the act of eating has a major impact in everyone's physical and mental health but also the choices we make when we cook has also a big impact on our planet and with those two in mind we believe that there is a big difference between creators and consumers when you are creating or you are cooking suddenly your awareness starts to grow you starting to care about where your ingredients come from or how the taste changes if those ingredients are in season or they are produced in a more controlled environment and when people start caring they tend to make better decisions that impact not only their health but also our environment we are an online community a global community that is available in more than 70 countries and support more than 30 languages which is important to understand some of the challenges that we have as a ml platform team we have more than 100 million users monthly and you can find more than 6 million recipes shared globally in the app you can browse recipes from ingredients that are in season to get inspired or you can follow authors like craig one of my favorites who uploads amazing recipes but you could also search by ingredients dish or cooking process etc machine learning is more available than ever in the past few years with the adoption of mlo practices and tools we have removed most of the pain points to deploy ml in production and that means that more ml teams have moved from working in isolation creating proof of concepts towards being deployed and distributed in product teams delivery teams or feature teams wherever the name your companies keep these type of teams as a result more ml is running it has moved now from running heavy batch jobs in the background towards running more and more online inference and with more ml models complex models available that means that the infrastructure requirement to run online inference in gpu comes along because we need those inference to run smoothly and quick for good user experience also as a machine learni
