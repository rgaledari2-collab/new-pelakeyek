export interface OrphanRecord {
  id: number;
  guardianName: string;
  guardianAge: string | number;
  guardianNationalId: string;
  childName: string;
  childLastName: string;
  fatherName: string;
  childNationalId: string;
  childAge: string | number;
  educationLevel: string;
  schoolName: string;
  healthStatus: string;
  address: string;
  phone: string;
}

export interface UnderprivilegedRecord {
  id: number;
  fullName: string;
  nationalId: string;
  phone: string;
  address: string;
}

export interface SchoolGradeStats {
  schoolName: string;
  preSchool: string | number;
  grade1: number;
  grade2: number;
  grade3: number;
  grade4: number;
  grade5: number;
  grade6: number;
  total: number;
}

export interface InfrastructureItem {
  name: string;
  area: string;
  stat: string;
  unit: string;
  type: 'health' | 'education' | 'culture' | 'gov' | 'religion';
}

export interface VillageData {
  id: string;
  name: string;
  x: number; // percentage on map (0 to 1)
  y: number; // percentage on map (0 to 1)
  tagline?: string;
  province: string;
  county: string;
  district: string;
  coordinates: string;
  population?: number;
  households?: number;
  studentsCount?: number;
  disabilityStats?: { label: string; count: number }[];
  infrastructure?: InfrastructureItem[];
  schools?: SchoolGradeStats[];
  orphans?: OrphanRecord[];
  underprivileged?: UnderprivilegedRecord[];
  notes?: string;
}

export const VILLAGES_DATA: VillageData[] = [
  {
    id: 'soureh',
    name: 'سوره',
    x: 0.670,
    y: 0.681,
    tagline: 'روستای مرکزی با بیشترین جمعیت و زیرساخت آموزشی و بهداشتی',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی، حومه غربی',
    coordinates: '48.1330° E, 30.4567° N',
    population: 4175,
    households: 1051,
    disabilityStats: [
      { label: 'شنوایی', count: 47 },
      { label: 'جسمی‌حرکتی', count: 92 },
      { label: 'بینایی', count: 44 },
      { label: 'ذهنی', count: 98 },
      { label: 'روانی', count: 15 },
      { label: 'صوت و گفتار', count: 2 },
    ],
    infrastructure: [
      { name: 'کتابخانه قلم چی', area: '۵۰۰ متر', stat: '۵۲۲', unit: 'عضو', type: 'culture' },
      { name: 'خانه بهداشت سوره ۱', area: '۲۰۰ متر', stat: '۴۹۸', unit: 'خانوار', type: 'health' },
      { name: 'مدرسه سوره', area: '۸۰۰ متر', stat: '۲۳۵', unit: 'دانش‌آموز', type: 'education' },
    ],
    schools: [
      { schoolName: 'رزمندگان', preSchool: '—', grade1: 13, grade2: 14, grade3: 16, grade4: 16, grade5: 18, grade6: 19, total: 96 },
      { schoolName: 'مطیری', preSchool: 20, grade1: 29, grade2: 19, grade3: 20, grade4: 17, grade5: 19, grade6: 15, total: 139 },
    ],
    orphans: [
      { id: 1, guardianName: 'زهرا مطوری', guardianAge: 57, guardianNationalId: '1816212344', childName: 'معصومه', childLastName: 'صنگور', fatherName: 'عبدالحسین', childNationalId: '1820516555', childAge: 14, educationLevel: 'هشتم', schoolName: 'کمیل', healthStatus: 'سالم', address: 'سوره – درب بندر – خ موسی بن جعفر (ع)', phone: '09337318902' },
      { id: 2, guardianName: 'سلوا سلیمانی', guardianAge: 56, guardianNationalId: '18248533', childName: 'سجاد', childLastName: 'سلیمانی', fatherName: 'هادی', childNationalId: '1820806774', childAge: 13, educationLevel: 'هفتم', schoolName: 'کمیل', healthStatus: 'سالم', address: 'سوره درب فعلیه – سه راهی', phone: '09374103605' },
      { id: 3, guardianName: 'فریده غانمی پور', guardianAge: 55, guardianNationalId: '1828247413', childName: 'امید', childLastName: 'خلیلی صالحی', fatherName: 'خسرو', childNationalId: '1820692167', childAge: 17, educationLevel: 'دهم', schoolName: 'شهر', healthStatus: 'سالم', address: 'سوره کوچک – خ روبروی تعاونی – روبروی مصلاوی', phone: '09383467763' },
      { id: 4, guardianName: 'عقیله صالحی', guardianAge: 45, guardianNationalId: '1820437922', childName: 'ام البنین', childLastName: 'صالحی اصل نژاد', fatherName: 'حاتم', childNationalId: '1820828867', childAge: 13, educationLevel: 'هشتم', schoolName: 'راهیان نور', healthStatus: 'سالم', address: 'سوره– روبروی انبار حقانی – خ امام حسن عسکری (ع)', phone: '09385898231' },
      { id: 5, guardianName: 'تسواهن عمرانی (مادربزرگ)', guardianAge: 62, guardianNationalId: '1829623321', childName: 'زهرا', childLastName: 'رابحی', fatherName: 'حسین', childNationalId: '1811302335', childAge: 16, educationLevel: 'هفتم', schoolName: 'راهیان نور', healthStatus: 'سالم', address: 'سوره – جنب حسینیه سید علی – خ مقاومت 2', phone: '09165977682' },
      { id: 6, guardianName: 'صبریه سکینی پور', guardianAge: 42, guardianNationalId: '3071243596', childName: 'رقیه', childLastName: 'قزاوی', fatherName: 'جبار', childNationalId: '1821140461', childAge: 5, educationLevel: 'پیش دبستانی', schoolName: '—', healthStatus: 'سالم', address: 'سوره - روبروی مدرسه رزمندگان', phone: '09051226088' },
      { id: 7, guardianName: 'ابتسام ادگیان پور', guardianAge: 35, guardianNationalId: '2150095084', childName: 'زهرا', childLastName: 'ادی', fatherName: 'اسماعیل', childNationalId: '1821037960', childAge: 8, educationLevel: 'دوم', schoolName: 'شهدای شلمچه', healthStatus: 'نیاز به خدمات دندانپزشکی', address: 'سوره - خ شلمچه 4', phone: '09386529928' },
      { id: 8, guardianName: 'شیخه سلمانی', guardianAge: 50, guardianNationalId: '1820941329', childName: 'اسما', childLastName: 'حمدی', fatherName: 'مهدی', childNationalId: '1820941329', childAge: 10, educationLevel: 'چهارم', schoolName: 'شهدای شلمچه', healthStatus: 'بیماری حلق و بینی', address: 'سوره – خ شلمچه 1 – کوچه بهار 1', phone: '09169342612' },
      { id: 9, guardianName: 'الهام عتیبی نژاد', guardianAge: 47, guardianNationalId: '4268867317', childName: 'آتنا', childLastName: 'رابحی', fatherName: 'عزیز', childNationalId: '1820967697', childAge: 10, educationLevel: 'چهارم', schoolName: 'شهدای شلمچه', healthStatus: 'سالم', address: 'سوره - شلمچه 4', phone: '09055185538' },
      { id: 10, guardianName: 'خدیجه مناحی اصل', guardianAge: 35, guardianNationalId: '1940090822', childName: 'یاسمین', childLastName: 'اصل محمودی سوره', fatherName: 'طالب', childNationalId: '1820490335', childAge: 23, educationLevel: 'دانشجو', schoolName: 'دانشگاه', healthStatus: 'سالم', address: 'سوره - خ فتح المبین - روبروی کوچه آزادی 5', phone: '09160968052' },
      { id: 11, guardianName: 'کوثر فحل', guardianAge: 39, guardianNationalId: '—', childName: 'حسن', childLastName: 'خضرایی منش', fatherName: 'مهدی', childNationalId: '1820964590', childAge: '—', educationLevel: '—', schoolName: '—', healthStatus: '—', address: 'سوره – روبروی جاده قطار - فدک 3- منزل سوم', phone: '09014035625' },
      { id: 12, guardianName: 'ماجده فحل', guardianAge: 36, guardianNationalId: '—', childName: 'عدنان', childLastName: 'علقمی زاده', fatherName: 'یاسین', childNationalId: '1820760332', childAge: '—', educationLevel: '—', schoolName: '—', healthStatus: '—', address: 'سوره – شلمچه 4 – جنب حسینیه زینبیه', phone: '09337572561' },
      { id: 13, guardianName: 'فضیله شمخانی', guardianAge: 46, guardianNationalId: '—', childName: 'فایزه', childLastName: 'باوی پور', fatherName: 'عبدالرحیم', childNationalId: '1744476853', childAge: '—', educationLevel: '—', schoolName: '—', healthStatus: '—', address: 'سوره – خ رزمندگان 3 – روبروی مدرسه رزمندگان', phone: '—' },
      { id: 14, guardianName: 'صدیقه سلیمانی', guardianAge: 48, guardianNationalId: '—', childName: 'حسن', childLastName: 'حمدی', fatherName: 'فالح', childNationalId: '1820648753', childAge: '—', educationLevel: '—', schoolName: '—', healthStatus: '—', address: 'سوره – خ فرعی 2 سمت راست – پلاک 230', phone: '09167328876' },
    ],
    underprivileged: [
      { id: 1, fullName: 'غنیه آلبوغبیش', nationalId: '1828540110', phone: '09363357880', address: 'سوره خیابان نیسی رو بروی دامداری قدیمی حقانی داخل کوچه سمت چپ' },
      { id: 2, fullName: 'نادیا نائلی', nationalId: '385062028', phone: '09360132942', address: 'سوره خیابان امام علی انتهای خیابان سمت چپ منزل یکی مونده آخر سرنبش ۳ راهی' },
      { id: 3, fullName: 'فاطمه سائری زاده', nationalId: '1829884018', phone: '09303653443', address: 'سوره خیابان امام علی ذوالفقار ۶ سمت چپ انتهای بن بست' },
      { id: 4, fullName: 'سکینه ربیع زاده', nationalId: '1828170232', phone: '09169315010', address: 'سوره خ ذوالفقار ۶ انتهای خیابان فرعی دوم سمت راست' },
      { id: 5, fullName: 'نرگس حنضلی زاده', nationalId: '1829016751', phone: '09399434927', address: 'سوره خیابان امام علی سمت راست نبش ذوالفقار درب کوچک کرم رنگ' },
      { id: 6, fullName: 'عفیفه حمدی', nationalId: '1751839494', phone: '09036158660', address: 'سوره خیابان رزمندگان ۲ سمت چپ انتهای خیابان' },
      { id: 7, fullName: 'سکینه سلیمانی', nationalId: '1751784411', phone: '09167243779', address: 'سوره خیابان اصلی کارواش به سمت حسینیه سید علی کردونی سمت راست' },
      { id: 8, fullName: 'مکیه سلمانیان اصل', nationalId: '1828243175', phone: '09166300844', address: 'سوره انتهای خیابان امام علی سمت چپ قبل از پل' },
      { id: 9, fullName: 'هدیه عرجیانی نژاد', nationalId: '934633282', phone: '09387034480', address: 'سوره خیابان شاهد ۱ سمت چپ منزل سوم انتهای فرعی' },
      { id: 10, fullName: 'زهرا آلبوغبیش', nationalId: '1816326313', phone: '09395149554', address: 'سوره خیابان اصلی جنب سوپرمارکت نرسیده به خیابان رزمندگان ۳' },
      { id: 11, fullName: 'قمرالملوک خطاوی', nationalId: '1828167282', phone: '09039501216', address: 'سوره ۲ فرعی فدک ۱ کوچه دوم سمت راست' },
      { id: 12, fullName: 'فضیله فحل', nationalId: '1890005096', phone: '09359084113', address: 'سوره ۲ فدک ۴ پشت راه‌آهن خیابان فدک ۴ سمت چپ منزل اول' },
      { id: 13, fullName: 'خدیجه صافی اصل', nationalId: '1828261092', phone: '09038766366', address: 'سوره ساکن خانه بهداشت' },
      { id: 14, fullName: 'امل غانمیان پور', nationalId: '1829643703', phone: '09363895866', address: 'سوره خ کارواش علی سمت چپ بعد از فرعی اول منزل دوم دو طبقه' },
      { id: 15, fullName: 'نادیا بنی طرف اصل', nationalId: '1815362731', phone: '09394486942', address: 'سوره خیابان مدرسه نوید اروند کوچه ایثار ۱ سمت چپ منزل اول' },
      { id: 16, fullName: 'فاطمه نائلی پور', nationalId: '1828242462', phone: '09370509663', address: 'سوره خیابان امام علی جنب ذوالفقار ۴ سرنبش' },
      { id: 17, fullName: 'فرحه حمدی', nationalId: '1751845834', phone: '09165073318', address: 'سوره ۱ فتح المبین جنب مدرسه نوید اروند کوچه ایثار ۱' },
      { id: 18, fullName: 'خدیجه مطیری', nationalId: '1828236322', phone: '09169871193', address: 'سوره جنب بندر خیابان شاهد ۶ اواسط کوچه جنب خانه بلوکی' },
      { id: 19, fullName: 'خدیجه محمودیان محرزی', nationalId: '1951157125', phone: '09374888329', address: 'سوره خ اصلی بین رزمندگان ۲ و ۳' },
      { id: 20, fullName: 'مهسا حسینی سوره', nationalId: '1861292066', phone: '09051903057', address: 'سوره ۲ شلمچه ۱ بهار ۳ خانه سر نبش سمت چپ' },
      { id: 21, fullName: 'منیژه حسین نژادسرحانی', nationalId: '1829349309', phone: '09374660170', address: 'سوره ۱ خ فتح المبین کوچه دوم سمت چپ منزل اول' },
      { id: 22, fullName: 'یاسمین جمیلی', nationalId: '1951257766', phone: '09332687897', address: 'سوره مقاومت ۱ سمت راست منزل سوم درب آبی رنگ' },
      { id: 23, fullName: 'فاطمه محیسن', nationalId: '5859344554', phone: '09032705380', address: 'سوره خیابان امام علی کوچه ذوالفقار ۶ سمت راست درب دوم' },
      { id: 24, fullName: 'مدلوله براجعی', nationalId: '1756209121', phone: '09168260657', address: 'سوره خیابان رزمندگان ۱ سمت چپ منزل چهارم' },
      { id: 25, fullName: 'سعید ثابت پور', nationalId: '1827870206', phone: '09165951743', address: 'سوره ۲ فدک ۱ انتهای خیابان سمت راست' },
      { id: 26, fullName: 'جبار ناصری حساوی', nationalId: '1828974031', phone: '09370906670', address: 'سوره ۲ کوچه فدک ۴ خ ساحلی راه‌آهن سمت راست' },
      { id: 27, fullName: 'حکیمه ناصری حساوی', nationalId: '1828247431', phone: '09356322753', address: 'سوره ۲ شلمچه ۶ آخرین منزل سمت راست' },
      { id: 28, fullName: 'ناصر حمدی', nationalId: '1828250074', phone: '09028219955', address: 'سوره روبه‌روی کوچه شاهد ۵ یا نانوایی منزل بلوکی' },
      { id: 29, fullName: 'رزاق حمدی', nationalId: '1751785191', phone: '09357236356', address: 'سوره خ اصلی زمین خالی روبروی شاهد ۱' },
      { id: 30, fullName: 'ایمان غزلاوی', nationalId: '1820097455', phone: '09304753502', address: 'سوره انتهای خیابان اصلی آخرین فرعی جنب درب بندر سرنبش شاهد ۶' },
      { id: 31, fullName: 'محمد مهدی پوربحرانی', nationalId: '5859862989', phone: '09168287594', address: 'سوره خ فتح المبین مدرسه رزمندگان کوچه ایثار ۲' },
      { id: 32, fullName: 'فاطمه باوی پور', nationalId: '1743468490', phone: '09376321083', address: 'سوره خیابان رزمندگان ۳ سمت چپ فرعی قبل از مدرسه' },
      { id: 33, fullName: 'عباس ورودی', nationalId: '1898272654', phone: '09379883997', address: 'سوره خ مرزداران بعد از کوچه امامت ۳' },
      { id: 34, fullName: 'خلف سلیمانی', nationalId: '1751847454', phone: '09166181782', address: 'خیابان پاسداران به سمت سوره بعد از عابربانک منزل سوم' },
      { id: 35, fullName: 'عبدالامیر هیجری', nationalId: '1828325139', phone: '09399092772', address: 'سوره ۲ نرسیده به پل سمت چپ جنب اولین کوچه' },
      { id: 36, fullName: 'فدیمه سلیمانی', nationalId: '1751785661', phone: '09045023819', address: 'سوره ابتدای خ رزمندگان ۳ سمت راست منزل دوم درب سبز' },
      { id: 37, fullName: 'مریم محمدیان هلالی', nationalId: '1828283721', phone: '09019540242', address: 'سوره خ کارواش به سمت حسینیه سید علی سمت چپ نبش فرعی آخر' },
      { id: 38, fullName: 'عبدالهادی بوعذار', nationalId: '1751831272', phone: '09030890382', address: 'سوره نرسیده به حسینیه سید علی کردونی کوچه انقلاب ۲' },
      { id: 39, fullName: 'نصیره خنفری', nationalId: '1899685952', phone: '09160109612', address: 'سوره بعد از پمپ بنزین روبروی مدرسه اروند خانه آخر سمت چپ' },
      { id: 40, fullName: 'رسول ناصری حساوی', nationalId: '2291315498', phone: '09303785352', address: 'سوره ۲ فدک ۴ سمت چپ انتهای بن بست' },
      { id: 41, fullName: 'شیرین ناصری', nationalId: '1820297462', phone: '09308714089', address: 'سوره خ رزمندگان ۳ روبروی مدرسه شهید مطیری سمت راست منزل اول' },
      { id: 42, fullName: 'فاطمه اشنود', nationalId: '1899506403', phone: '09029046784', address: 'سوره خیابان شاهد سمت راست منزل دوم جنب نانوایی' },
      { id: 43, fullName: 'فاضل حمدی', nationalId: '1820119165', phone: '09053950083', address: 'سوره درب بندر خ شاهد ۱ سمت راست منزل اول بعد از منزل نیمه‌کاره' },
      { id: 44, fullName: 'محمدعلی غزلاوی', nationalId: '1756246841', phone: '09377638744', address: 'سوره خیابان رزمندگان ۳ کوچه آزادی ۴ فرعی سمت راست' },
      { id: 45, fullName: 'محمود سلیمانی', nationalId: '6629951344', phone: '09028227699', address: 'سوره خ مقاومت ۲ منزل سوم سمت راست' },
      { id: 46, fullName: 'حمیده سلیمانی', nationalId: '1741572010', phone: '09028227699', address: 'سوره خ مقاومت ۲ منزل سوم سمت راست' },
      { id: 47, fullName: 'ابوالفضل موسوی', nationalId: '1820603636', phone: '09353365771', address: 'سوره انتهای خ مقاومت ۱ سمت راست منزل یکی مانده به آخر' },
      { id: 48, fullName: 'مریم خرسانی نژاد', nationalId: '1170780164', phone: '09169316020', address: 'سوره خ امام علی ذوالفقاری بعد از پل سمت چپ منزل سوم' },
      { id: 49, fullName: 'احمد براجعه', nationalId: '1740777697', phone: '09168260545', address: 'سوره خ اصلی سرنبش رزمندگان ۲ منزل اول' },
      { id: 50, fullName: 'راضیه حمیدی', nationalId: '1756671672', phone: '09044395562', address: 'سوره ابتدای خیابان رزمندگان ۳ سمت راست نبش فرعی اول' },
      { id: 51, fullName: 'فاطمه محیسن', nationalId: '1820746526', phone: '09166313893', address: 'سوره خ مقاومت اصلی انقلاب ۴ بعد از حسینیه سید علی کردونی' },
      { id: 52, fullName: 'علیرضا فیصلی', nationalId: '1820866696', phone: '09019204214', address: 'سوره ۲ شلمچه ۱ اولین فرعی سمت چپ اولین منزل' },
      { id: 53, fullName: 'اسعد باوی پور', nationalId: '1829572407', phone: '09376321083', address: 'سوره خیابان رزمندگان ۳ سمت چپ فرعی قبل از مدرسه' },
      { id: 54, fullName: 'سهیلا غزلاوی', nationalId: '1820090434', phone: '09372355892', address: 'سوره خ رزمندگان ۳ فرعی سوم آخرین منزل آزادی ۴' },
      { id: 55, fullName: 'نعیم عاشور نژاد', nationalId: '1828243973', phone: '09050998094', address: 'سوره خ امام علی سمت چپ منزل دوطبقه بعد از فرعی اول' },
      { id: 56, fullName: 'زینب حمودی', nationalId: '1820002349', phone: '09352991565', address: 'سوره خ امام علی ذوالفقار ۶ بعد از پیچ دوم (مددجوی ناشنوا - هماهنگی قبل از مراجعه)' },
    ],
  },
  {
    id: 'ariz',
    name: 'عریض',
    x: 0.500,
    y: 0.120,
    tagline: 'روستای معراج در محور شمالی با نیازهای توسعه آموزشی و حمایتی',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی، حومه غربی',
    coordinates: '48.1345° E, 30.4913° N',
    population: 281,
    households: 74,
    infrastructure: [
      { name: 'مدرسه امام رضایی‌ها', area: '۱,۲۰۰ متر', stat: '۲۴', unit: 'دانش‌آموز', type: 'education' },
    ],
    schools: [
      { schoolName: 'جمعیت امام رضایی‌ها', preSchool: 0, grade1: 2, grade2: 6, grade3: 5, grade4: 2, grade5: 4, grade6: 5, total: 24 },
    ],
    orphans: [
      { id: 1, guardianName: 'سیده اقدس مفتی عریض', guardianAge: 44, guardianNationalId: '1728293628', childName: 'مریم', childLastName: 'عریضاوی', fatherName: 'عبدالامام', childNationalId: '1820939261', childAge: 11, educationLevel: 'پنجم', schoolName: 'امام رضایی‌ها', healthStatus: 'سالم', address: 'روستای عریض - معراج ۲', phone: '09076792730' },
    ],
    underprivileged: [
      { id: 1, fullName: 'سکینه عیدیان پور', nationalId: '1899611037', phone: '09030137830', address: 'پل نو روستای عریض انتهای معراج ۴' },
      { id: 2, fullName: 'حمیده روزی زاده', nationalId: '—', phone: '09045206539', address: 'پل نو روستای عریض خ معراج ۹ بعد از حسینیه منزل بلوکی' },
      { id: 3, fullName: 'جلال قویشاوی', nationalId: '5279774529', phone: '09307499368', address: 'روستای عریض خ اصلی معراج ۹ روبروی مسجد' },
      { id: 4, fullName: 'نسیمه معرفی', nationalId: '1820465152', phone: '09163328512', address: 'روستای عریض خیابان اصلی بین معراج ۲ و ۳' },
    ],
  },
  {
    id: 'pol-now',
    name: 'پل نو',
    x: 0.550,
    y: 0.430,
    tagline: 'روستای کلیدی در محور جاده شلمچه با دو مدرسه و مرکز بهداشت',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی، حومه غربی',
    coordinates: '48.1272° E, 30.4711° N',
    population: 1874,
    households: 592,
    infrastructure: [
      { name: 'خانه بهداشت پل نو', area: '۲۰۰ متر', stat: '۵۹۲', unit: 'خانوار', type: 'health' },
      { name: 'مدرسه حر بن ریاحی', area: '۸۰۰ متر', stat: '۹۴', unit: 'دانش‌آموز', type: 'education' },
      { name: 'دهیاری پل نو', area: '۲۰۰ متر', stat: 'فعال', unit: 'مرکز', type: 'gov' },
      { name: 'خانه عالم', area: '۳۰۰ متر', stat: '۱', unit: 'واحد', type: 'religion' },
    ],
    schools: [
      { schoolName: 'حر بن ریاحی (پسرانه)', preSchool: '—', grade1: 11, grade2: 10, grade3: 8, grade4: 7, grade5: 3, grade6: 15, total: 54 },
      { schoolName: 'حر بن ریاحی (دخترانه)', preSchool: '—', grade1: 4, grade2: 11, grade3: 7, grade4: 6, grade5: 8, grade6: 4, total: 40 },
    ],
    orphans: [
      { id: 1, guardianName: 'جواهر سلیمانی', guardianAge: 30, guardianNationalId: '1829567251', childName: 'کرار', childLastName: 'سلیمانی', fatherName: 'سعید', childNationalId: '1821068858', childAge: 7, educationLevel: 'اول', schoolName: 'حر بن ریاحی', healthStatus: 'سالم', address: 'پل نو - ولایت ۵ - روبروی حسینیه', phone: '09309552337' },
      { id: 2, guardianName: 'فاطمه غزلی', guardianAge: 53, guardianNationalId: '—', childName: 'مهدی', childLastName: 'غزلی', fatherName: 'رحیم', childNationalId: '1820587444', childAge: 19, educationLevel: 'بزرگسالان', schoolName: 'شهر', healthStatus: 'سالم', address: 'پل نو - شهرک اول - خ دوم', phone: '09331522544' },
      { id: 3, guardianName: 'سکینه هجر', guardianAge: 38, guardianNationalId: '2432947703', childName: 'ثریا', childLastName: 'حساوی نژاد', fatherName: 'احمد', childNationalId: '1821091531', childAge: 7, educationLevel: 'اول', schoolName: 'شهدای شلمچه', healthStatus: 'سالم', address: 'پل نو - جاده شلمچه - پشت مدرسه انقلاب', phone: '09380591304' },
      { id: 4, guardianName: 'هیفاء سلیمانی', guardianAge: 34, guardianNationalId: '1820100405', childName: 'رقیه', childLastName: 'سلیمانی', fatherName: 'حمید', childNationalId: '1748594818', childAge: 10, educationLevel: 'چهارم', schoolName: 'شهدای شلمچه', healthStatus: 'سالم', address: 'پل نو - خیابان اصلی - ولایت ۷', phone: '09398303973' },
      { id: 5, guardianName: 'سمیره عیدانی پور', guardianAge: '—', guardianNationalId: '—', childName: 'فاطمه', childLastName: 'فرحانی معموری', fatherName: 'محمدجواد', childNationalId: '1820592316', childAge: '—', educationLevel: '—', schoolName: '—', healthStatus: 'سالم', address: 'پل نو - جاده شلمچه - خ ساحلی فدک ۳ منزل چهارم', phone: '09373988324' },
      { id: 6, guardianName: 'بشری عیاشی', guardianAge: 60, guardianNationalId: 'اتباع عراقی', childName: 'حامد', childLastName: 'عیاشی', fatherName: 'حسین', childNationalId: '1820568210', childAge: 22, educationLevel: 'دوم', schoolName: 'ترک تحصیل', healthStatus: 'سالم', address: 'پل نو ولایت ۶', phone: '09383711450' },
      { id: 7, guardianName: 'شهین نیسی', guardianAge: 48, guardianNationalId: '1827931371', childName: 'مهدی', childLastName: 'سگر', fatherName: 'علی', childNationalId: '1820695271', childAge: 17, educationLevel: 'یازدهم', schoolName: 'شهر', healthStatus: 'سالم', address: 'پل نو - بعد از مدرسه - کوچه معلم', phone: '09046602553' },
    ],
    underprivileged: [
      { id: 1, fullName: 'اصیله ناصری پورسوره', nationalId: '1828127221', phone: '09308718261', address: 'پل نو جاده شلمچه شهرک اول خ پل نو ۷ سمت راست منزل هفتم' },
      { id: 2, fullName: 'غیده مجدماوی', nationalId: '1828471119', phone: '09306693492', address: 'پل نو شهرک اول خ ولایت ۴ پل نو ۴ سمت چپ منزل دوم' },
      { id: 3, fullName: 'زهرا عیدان', nationalId: '1828193402', phone: '09385699171', address: 'پل نو شهرک اول ولایت ۳ خین ۶ سمت چپ منزل دوم' },
      { id: 4, fullName: 'جابر فرحانی', nationalId: '1829601733', phone: '09396071614', address: 'پل نو شهرک اول خیابان پل نو ۳ انتهای خیابان منزل پنجم' },
      { id: 5, fullName: 'دیوان ادگیان پور', nationalId: '1828294284', phone: '09169288793', address: 'پل نو شهرک اول ولایت ۱ خین ۳ سمت چپ درب چهارم' },
      { id: 6, fullName: 'فرحان شریف', nationalId: '1818915571', phone: '09034339448', address: 'پل نو شهرک اول خیابان پل نو ۶ سمت راست' },
      { id: 7, fullName: 'عبدالهادی ضرغام پور', nationalId: '1828167320', phone: '09378806583', address: 'شهرک اول ولایت ۲ پل نو ۱ سمت راست منزل سوم' },
      { id: 8, fullName: 'حکیمه هذبری', nationalId: '1828294081', phone: '09335099527', address: 'پل نو شهرک اول خ پل نو ۸ منزل چهارم' },
      { id: 9, fullName: 'صفیه هیحر', nationalId: '1815759941', phone: '09052253725', address: 'پل نو شهرک اول خیابان پل نو ۵ سمت چپ منزل اول' },
      { id: 10, fullName: 'هاشمیه موسوی', nationalId: '1828180181', phone: '09366157542', address: 'شهرک اول چهارراه اصلی جنب حسینیه ابوالفضل روبه‌روی پارک' },
      { id: 11, fullName: 'محمود حبیبی نیا', nationalId: '1829646745', phone: '09379209466', address: 'پل نو شهرک اول خیابان خین ۸ سمت راست' },
      { id: 12, fullName: 'لفته تمیمی', nationalId: '1828071145', phone: '09027244582', address: 'پل نو شهرک اول خیابان پل نو ۲ خیابان مدرسه' },
      { id: 13, fullName: 'هادی تمیمی', nationalId: '1820848991', phone: '09054756357', address: 'پل نو شهرک اول خ پل نو ۲ جنب مدرسه حر بن ریاحی کوچه ۶ متری' },
      { id: 14, fullName: 'زینب هزامی', nationalId: '3430412358', phone: '09378002433', address: 'پل نو شهرک اول ولایت ۳ خ خین ۴ سمت چپ منزل اول' },
      { id: 15, fullName: 'مصطفی ضرغام پور', nationalId: '1820594416', phone: '09301861349', address: 'پل نو شهرک اول خیابان خین ۲ سمت چپ' },
      { id: 16, fullName: 'مهدی براجعه', nationalId: '1820522611', phone: '09055929824', address: 'شهرک اول خ پل نو ۹ منزل سوم' },
      { id: 17, fullName: 'عبدالرحیم معاوی', nationalId: '1820413322', phone: '09375230549', address: 'پل نو شهرک اول خ پل نو ۳ سمت چپ منزل آخر' },
      { id: 18, fullName: 'مریم غزلی', nationalId: '1820517871', phone: '09370405237', address: 'پل نو شهرک اول خ پل نو ۳ سمت چپ جنب بن بست' },
      { id: 19, fullName: 'وفاء مهاجران', nationalId: '1818576422', phone: '09033607385', address: 'پل نو شهرک اول انتهای ولایت ۳ خین ۴ سمت راست' },
      { id: 20, fullName: 'احمد حسائی پور', nationalId: '1870513894', phone: '09386798481', address: 'پل نو شهرک اول ولایت ۳ خین ۴' },
      { id: 21, fullName: 'لیلا براجعه', nationalId: '1820522628', phone: '09055929824', address: 'پل نو شهرک اول خ پل نو ۹ منزل سوم' },
      { id: 22, fullName: 'معصومه جران', nationalId: '1816081906', phone: '09373806153', address: 'پل نو شهرک اول خیابان ولایت ۴ پل نو ۵ سمت راست' },
    ],
  },
  {
    id: 'jadideh',
    name: 'جدیده',
    x: 0.812,
    y: 0.795,
    tagline: 'روستای دارای مرکز جامع خدمات سلامت منطقه',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی، حومه غربی',
    coordinates: '48.1450° E, 30.4420° N',
    population: 3200,
    households: 850,
    disabilityStats: [
      { label: 'شنوایی', count: 30 },
      { label: 'جسمی‌حرکتی', count: 70 },
      { label: 'بینایی', count: 25 },
      { label: 'ذهنی', count: 60 },
      { label: 'روانی', count: 10 },
      { label: 'صوت و گفتار', count: 1 },
    ],
    infrastructure: [
      { name: 'مرکز جامع سلامت جدیده', area: '۶۰۰ متر', stat: 'پزشک ثابت', unit: 'مرکز', type: 'health' },
    ],
  },
  {
    id: 'sad-dastgah',
    name: 'صد دستگاه',
    x: 0.890,
    y: 0.880,
    tagline: 'منطقه مسکونی حومه خرمشهر با بافت فشرده',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1520° E, 30.4350° N',
    population: 2500,
    households: 600,
    disabilityStats: [
      { label: 'شنوایی', count: 20 },
      { label: 'جسمی‌حرکتی', count: 50 },
      { label: 'بینایی', count: 20 },
      { label: 'ذهنی', count: 45 },
      { label: 'روانی', count: 5 },
      { label: 'صوت و گفتار', count: 1 },
    ],
  },
  {
    id: 'darband-gharbi',
    name: 'دربند غربی',
    x: 0.785,
    y: 0.890,
    tagline: 'روستای حاشیه رودخانه با ظرفیت‌های کشاورزی و نخلداری',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1400° E, 30.4310° N',
    population: 1800,
    households: 400,
    disabilityStats: [
      { label: 'شنوایی', count: 15 },
      { label: 'جسمی‌حرکتی', count: 30 },
      { label: 'بینایی', count: 10 },
      { label: 'ذهنی', count: 25 },
      { label: 'روانی', count: 3 },
      { label: 'صوت و گفتار', count: 0 },
    ],
  },
  {
    id: 'darband-sharqi',
    name: 'دربند شرقی',
    x: 0.655,
    y: 0.865,
    tagline: 'روستای شرقی مجاور نخلستان‌ها و کانال‌های آب',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1310° E, 30.4340° N',
  },
  {
    id: 'sarhaniyeh-avval',
    name: 'سرحانیه اول',
    x: 0.850,
    y: 0.710,
    tagline: 'منطقه سرحانیه با نیازمندی‌های ارتقای امکانات خدماتی',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1490° E, 30.4510° N',
  },
  {
    id: 'sarhaniyeh-sofla',
    name: 'سرحانیه سفلی',
    x: 0.880,
    y: 0.640,
    tagline: 'بخش جنوبی سرحانیه مجاور محور دسترسی اصلی',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1530° E, 30.4590° N',
  },
  {
    id: 'maslavi',
    name: 'مصلاوی',
    x: 0.730,
    y: 0.510,
    tagline: 'روستای مجاور محور سوره و پل نو',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1380° E, 30.4680° N',
  },
  {
    id: 'maslavi2',
    name: 'مصلاوی ۲',
    x: 0.800,
    y: 0.470,
    tagline: 'بخش الحاقی روستای مصلاوی',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1420° E, 30.4710° N',
  },
  {
    id: 'shahrak-sadat',
    name: 'شهرک سادات',
    x: 0.830,
    y: 0.380,
    tagline: 'شهرک مسکونی محور شمالی غرب خرمشهر',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1460° E, 30.4790° N',
  },
  {
    id: 'shahrak-sevvom',
    name: 'شهرک سوم',
    x: 0.120,
    y: 0.190,
    tagline: 'نقطه غربی نزدیک به نوار مرزی شلمچه',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.0750° E, 30.4850° N',
  },
  {
    id: 'mofti-ariz',
    name: 'مفتی عریض',
    x: 0.680,
    y: 0.090,
    tagline: 'منطقه کشاورزی و دامپروری منتهی‌الیه شمال غربی',
    province: 'خوزستان',
    county: 'خرمشهر',
    district: 'مرکزی',
    coordinates: '48.1390° E, 30.5010° N',
  },
];

export const REGIONAL_HEALTH_INFO = {
  title: 'شبکه و دسترسی سلامت منطقه غرب خرمشهر',
  centers: [
    {
      title: 'مراکز جامع سلامت',
      desc: 'جدیده و امام حسین؛ با حضور پزشک ثابت در مرکز و پزشک چرخشی در خانه‌های بهداشت روستایی.',
      badge: 'پوشش عمومی',
    },
    {
      title: 'خدمات و مراقبت‌های پایه',
      desc: 'بهداشت خانواده و باروری، واکسیناسیون کشوری، دندانپزشکی، تغذیه، سلامت روان، ویزیت پزشک عمومی و داروخانه.',
      badge: 'پایه و پیشگیری',
    },
    {
      title: 'زمان دسترسی در ساعات کاری',
      desc: 'حداکثر ۱۰ دقیقه تا نزدیک‌ترین خانه بهداشت برای دورترین روستاهای تحت پوشش محور شلمچه.',
      badge: '۱۰ دقیقه',
    },
    {
      title: 'زمان دسترسی خارج از ساعت اداری',
      desc: '۲۰ الی ۳۰ دقیقه تا بیمارستان‌های شهر خرمشهر (شهید بهشتی و ولیعصر)؛ کمبود فوریت‌های شبانه‌روزی محلی از مهم‌ترین چالش‌های مردم است.',
      badge: 'چالش حیاتی',
    },
  ],
  source: 'برگرفته از گزارش پایش میدانی «خدمات درمانی و فعالیت» - جمعیت امام‌رضایی‌ها',
};
