---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["AI ML"]
speakers: ["Xiaowei Hu", "Second State"]
sched_url: https://kccnceu2024.sched.com/event/1YeRH/create-cloud-native-agents-and-extensions-for-llms-xiaowei-hu-second-state
youtube_search_url: https://www.youtube.com/results?search_query=Create+Cloud+Native+Agents+and+Extensions+for+LLMs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Create Cloud Native Agents and Extensions for LLMs - Xiaowei Hu, Second State

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]]
- País/cidade: France / Paris
- Speakers: Xiaowei Hu, Second State
- Schedule: https://kccnceu2024.sched.com/event/1YeRH/create-cloud-native-agents-and-extensions-for-llms-xiaowei-hu-second-state
- Busca YouTube: https://www.youtube.com/results?search_query=Create+Cloud+Native+Agents+and+Extensions+for+LLMs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Create Cloud Native Agents and Extensions for LLMs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRH/create-cloud-native-agents-and-extensions-for-llms-xiaowei-hu-second-state
- YouTube search: https://www.youtube.com/results?search_query=Create+Cloud+Native+Agents+and+Extensions+for+LLMs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q8AVAwdCqYk
- YouTube title: Create Cloud Native Agents and Extensions for LLMs - Xiaowei Hu, Second State
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/create-cloud-native-agents-and-extensions-for-llms/q8AVAwdCqYk.txt
- Transcript chars: 27686
- Keywords: server, wasm, application, python, language, device, question, models, download, gpu, create, applications, another, source, command, single, native, install

### Resumo baseado na transcript

hello everyone welcome to my session U my name is W who and I'm one of the U maintainer of the cncf was my project um hello everyone my name is Michael Yan and uh um I'm also uh the maintainer of the wage project uh so today Mike and I will talk about uh creating cognitive apps uh we will use uh Lage it's uh lightweight and posable runtime based on the world M run time um so let's get started so uh the current Tex stack for our wasm is uh is application that compiled from rust and then you know um and then we demonstrated here yeah so let's uh so this is the first EXO we just create um open a compatible AP for the gamma Tob model and um as in it it's about it cost about $2,000 we use it in our office as a coding assistant so we run the uh uh code Lama uh model on that on that device to hook up with all the visual studio idees that we have

### Excerpt da transcript

hello everyone welcome to my session U my name is W who and I'm one of the U maintainer of the cncf was my project um hello everyone my name is Michael Yan and uh um I'm also uh the maintainer of the wage project uh so today Mike and I will talk about uh creating cognitive apps uh we will use uh Lage it's uh lightweight and posable runtime based on the world M run time um so let's get started so uh the current Tex stack for our applications is dominated by python apparently we use pyto and python to do erence and if you want to um build some LM agents when you where we use launching and python however python has its problems U first it's heavyweight because there are lots of complex dependencies with python um the IM the picture here is the official Pyon doer image U from the U from this picture we can see that um uh py doer image can be 4 gabes it's almost the same size of a light language model like lamb 27b so it's very huge and um um one more thing is that the uh uh the the python based umm application is not posable um uh different uh GPU drivers requires different Docker images also from this picture we can see that um um C 11 and C 12 uh sh uh uh the do image for k 11 and 12 is a is a is different do images so this is the pro the problem of python so how about we use a native comp applications such like native Russ or C applications yes they are much smaller than python but um those native applications are not pable U if we want to run the same application on MacBook and an N media GPU then we need to recom recompare these applications on the device but um um kubernetes can only exract binary artifacts so uh that's the problem with python and um Native applications how can we achieve the how can we solve this problems um all right yeah so um I I think this is U one of the common thread in this on cucon is that how do we make kuber kubernetes work better with uh machine learning and uh large language model workloads um as we have seen there's uh um you know as we have shown those P pytho images are gigabytes measured in gigabytes right you know it's uh it's very heavy even in the in in a cloud environment and uh um the native applications apparently uh they are not portable it's not not just the problem with kubernetes we are going all the way back to the problem where if I develop something on my laptop I can never be guaranteed this thing going to run on the server or on or on another device because they may have a different GPU right you know it's
