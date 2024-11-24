import type Tag from "./Tag";

export default interface NewsBase {
    title: string,
    text: string,
    tags: Tag
}