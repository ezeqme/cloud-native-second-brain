---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Runtime Containers"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQhr/wasmcloud-declarative-webassembly-orchestration-for-cloud-native-applications-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=wasmCloud%3A+Declarative+WebAssembly+Orchestration+for+Cloud+Native+Applications+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# wasmCloud: Declarative WebAssembly Orchestration for Cloud Native Applications | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Runtime Containers]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQhr/wasmcloud-declarative-webassembly-orchestration-for-cloud-native-applications-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=wasmCloud%3A+Declarative+WebAssembly+Orchestration+for+Cloud+Native+Applications+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre wasmCloud: Declarative WebAssembly Orchestration for Cloud Native Applications | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQhr/wasmcloud-declarative-webassembly-orchestration-for-cloud-native-applications-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=wasmCloud%3A+Declarative+WebAssembly+Orchestration+for+Cloud+Native+Applications+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5ue8p6jxYyM
- YouTube title: wasmCloud: Declarative WebAssembly Orchestration for Cloud Native Applications | Project Lightnin...
- Match score: 1.049
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/wasmcloud-declarative-webassembly-orchestration-for-cloud-native-appli/5ue8p6jxYyM.txt
- Transcript chars: 6560
- Keywords: assembly, platform, application, standards, applications, components, native, wasm, actually, important, binary, component, common, runtime, little, running, declarative, boundary

### Resumo baseado na transcript

hey everyone uh welcome to the cncf wasm cloud project update we are a Sandbox project in the cncf uh primarily under the application platform or the scheduling and orchestration section uh I like to say that we're in the same category as kubernetes just a smaller box kind of all the way in the bottom right corner so that's very fun you all have probably heard of the word uh Cloud before but not all of you have heard of uh WM before so I always love asking this

### Excerpt da transcript

hey everyone uh welcome to the cncf wasm cloud project update we are a Sandbox project in the cncf uh primarily under the application platform or the scheduling and orchestration section uh I like to say that we're in the same category as kubernetes just a smaller box kind of all the way in the bottom right corner so that's very fun you all have probably heard of the word uh Cloud before but not all of you have heard of uh WM before so I always love asking this question who has heard of web assembly or wasum in this room actually I love the ratio of that going out every single year um so I will do a quick just run through on what wasum is just for the folks who haven't heard of it because it's important it is the core piece of the wasum cloud project uh which is our unit of compute for the application platform and it really is just like a tiny virtual machine you write code in a language of your choice you compile it to web assembly instead of a native binary or something that you would execute as a script and then it can run on anywhere that a wasm runtime can run which is a browser or on the server side on x86 on arm Etc so this is really important for us in order to work as an app platform our our actual applications are composed of web assembly components and what that is is basically just a small little piece a small architecture and operating system agnostic binary it actually does look like assembly but like I said you're just writing code and then compiling it to that and every single web assembly component has a set of imports and exports you can kind of think of this like the cffi boundary that's how it actually gets things done and we operate with a set of common imports and exports like HTTP blob store key value logging these common application components uh that you use in Cloud native applications every day so these components you can not only build applications with them you can compose them together uh which is a core piece of how we have you know if you have multiple different microservices in your application they talk to each other over this component boundary and uh the really important part of this is in the web assembly specification in the standard is a very strong uh security boundary that's driven by these common interfaces and these different components actually don't share anything when they run so that is a little bit of a preamble and preview it sounds like a lot of people knew about web assembly already which is awesome so jus
