---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Asheesh Goja", "Amazon Web Services"]
sched_url: https://kccncna2023.sched.com/event/1R2sy/kube-of-thoughts-scaling-generative-ai-models-with-kubernetes-and-inference-decision-trees-asheesh-goja-amazon-web-services
youtube_search_url: https://www.youtube.com/results?search_query=Kube+of+Thoughts+%E2%80%93+Scaling+Generative+AI+Models+with+Kubernetes+and+Inference+Decision+Trees+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kube of Thoughts – Scaling Generative AI Models with Kubernetes and Inference Decision Trees - Asheesh Goja, Amazon Web Services

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Asheesh Goja, Amazon Web Services
- Schedule: https://kccncna2023.sched.com/event/1R2sy/kube-of-thoughts-scaling-generative-ai-models-with-kubernetes-and-inference-decision-trees-asheesh-goja-amazon-web-services
- Busca YouTube: https://www.youtube.com/results?search_query=Kube+of+Thoughts+%E2%80%93+Scaling+Generative+AI+Models+with+Kubernetes+and+Inference+Decision+Trees+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kube of Thoughts – Scaling Generative AI Models with Kubernetes and Inference Decision Trees.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sy/kube-of-thoughts-scaling-generative-ai-models-with-kubernetes-and-inference-decision-trees-asheesh-goja-amazon-web-services
- YouTube search: https://www.youtube.com/results?search_query=Kube+of+Thoughts+%E2%80%93+Scaling+Generative+AI+Models+with+Kubernetes+and+Inference+Decision+Trees+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ewN3wbPsWPg
- YouTube title: Kube of Thoughts – Scaling Generative AI Models with Kubernetes and Inference Decisi... Asheesh Goja
- Match score: 1.01
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kube-of-thoughts-scaling-generative-ai-models-with-kubernetes-and-infe/ewN3wbPsWPg.txt
- Transcript chars: 40259
- Keywords: thought, strategy, solution, language, answer, prompt, custom, thoughts, operator, partial, search, solving, models, problems, complexity, complex, trying, algorithm

### Resumo baseado na transcript

a warm welcome to cucon 2023 to this beautiful city of Chicago I'm so happy to be here and I'm grateful to each one of you for choosing to be at my session today we are about to explore how kubernetes and inflence decision trees can help us efficiently scale gen inferencing for solving complex reasoning problems so without further Ado let's Jump Right In we have an exciting exciting journey ahead and plenty to share a quick introduction about me uh i c ly work as a principal Solutions

### Excerpt da transcript

a warm welcome to cucon 2023 to this beautiful city of Chicago I'm so happy to be here and I'm grateful to each one of you for choosing to be at my session today we are about to explore how kubernetes and inflence decision trees can help us efficiently scale gen inferencing for solving complex reasoning problems so without further Ado let's Jump Right In we have an exciting exciting journey ahead and plenty to share a quick introduction about me uh i c ly work as a principal Solutions architect at for AWS and my daily Adventures include collaborating and co- innovating with some of our largest isv customers right in the heart of gen world the San Francisco Bay Area previously I worked uh with Cisco with the emerging technology and incubation team uh I believe it's now called Cisco out shift anyone from Cisco here great team I loved working there I miss you guys so my journey with kubernetes goes all the way back to 2017 uh at UPS where I architecturally established UPS's first private Cloud using kubernetes with open shift any open shift guys here Awesome Again great product I learned a lot from you guys back then I was a student uh so exploring the intersection of kubernetes and machine learning has been an active area of interest for me since back in 2021 at coupon at La I talked about the inter ction of kubernetes and AI That's a link to my talk and a Blog and today I'm thrilled to talk about my exploration into the world of kubernetes and jni you guys ready all right so to kick things off I'll start with a simple math problem if somebody has downloaded my slides U uh you might be able to get a sneak peek at that uh but it's still a surprise um so I'll start with a a math game from there we will examine the the challenges that uh the most state-of art large language models today have in solving such complex problems and we'll see how a prompting strategy called tree of thoughts approaches such complex reasoning problems then I'll talk about the efficiency and complexity challenges uh and how to use various software patterns and hosting this tree of thought strategy on kubernetes can make tree of thought strategy not just functional but practical and efficient and what better way to bring it to life then with a live demo I'll show you a tree of thought strategy solving a complex math problem on a kubernetes cluster so to wrap things up I share some of my concluding thoughts on the future of tree of thought and its Evolution so in order to understand uh t
