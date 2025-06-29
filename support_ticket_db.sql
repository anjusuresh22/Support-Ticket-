-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 15, 2025 at 11:39 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `support_ticket_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add bill', 7, 'add_bill'),
(26, 'Can change bill', 7, 'change_bill'),
(27, 'Can delete bill', 7, 'delete_bill'),
(28, 'Can view bill', 7, 'view_bill'),
(29, 'Can add chat', 8, 'add_chat'),
(30, 'Can change chat', 8, 'change_chat'),
(31, 'Can delete chat', 8, 'delete_chat'),
(32, 'Can view chat', 8, 'view_chat'),
(33, 'Can add login', 9, 'add_login'),
(34, 'Can change login', 9, 'change_login'),
(35, 'Can delete login', 9, 'delete_login'),
(36, 'Can view login', 9, 'view_login'),
(37, 'Can add menu', 10, 'add_menu'),
(38, 'Can change menu', 10, 'change_menu'),
(39, 'Can delete menu', 10, 'delete_menu'),
(40, 'Can view menu', 10, 'view_menu'),
(41, 'Can add menutype', 11, 'add_menutype'),
(42, 'Can change menutype', 11, 'change_menutype'),
(43, 'Can delete menutype', 11, 'delete_menutype'),
(44, 'Can view menutype', 11, 'view_menutype'),
(45, 'Can add menustock', 12, 'add_menustock'),
(46, 'Can change menustock', 12, 'change_menustock'),
(47, 'Can delete menustock', 12, 'delete_menustock'),
(48, 'Can view menustock', 12, 'view_menustock'),
(49, 'Can add cart', 13, 'add_cart'),
(50, 'Can change cart', 13, 'change_cart'),
(51, 'Can delete cart', 13, 'delete_cart'),
(52, 'Can view cart', 13, 'view_cart'),
(53, 'Can add orderlist', 14, 'add_orderlist'),
(54, 'Can change orderlist', 14, 'change_orderlist'),
(55, 'Can delete orderlist', 14, 'delete_orderlist'),
(56, 'Can view orderlist', 14, 'view_orderlist'),
(57, 'Can add staff', 15, 'add_staff'),
(58, 'Can change staff', 15, 'change_staff'),
(59, 'Can delete staff', 15, 'delete_staff'),
(60, 'Can view staff', 15, 'view_staff'),
(61, 'Can add user', 16, 'add_user'),
(62, 'Can change user', 16, 'change_user'),
(63, 'Can delete user', 16, 'delete_user'),
(64, 'Can view user', 16, 'view_user'),
(65, 'Can add recommendation', 17, 'add_recommendation'),
(66, 'Can change recommendation', 17, 'change_recommendation'),
(67, 'Can delete recommendation', 17, 'delete_recommendation'),
(68, 'Can view recommendation', 17, 'view_recommendation'),
(69, 'Can add complaint', 18, 'add_complaint'),
(70, 'Can change complaint', 18, 'change_complaint'),
(71, 'Can delete complaint', 18, 'delete_complaint'),
(72, 'Can view complaint', 18, 'view_complaint'),
(73, 'Can add amc', 19, 'add_amc'),
(74, 'Can change amc', 19, 'change_amc'),
(75, 'Can delete amc', 19, 'delete_amc'),
(76, 'Can view amc', 19, 'view_amc'),
(77, 'Can add rating', 20, 'add_rating'),
(78, 'Can change rating', 20, 'change_rating'),
(79, 'Can delete rating', 20, 'delete_rating'),
(80, 'Can view rating', 20, 'view_rating');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(19, 'EDPApp', 'amc'),
(7, 'EDPApp', 'bill'),
(13, 'EDPApp', 'cart'),
(8, 'EDPApp', 'chat'),
(18, 'EDPApp', 'complaint'),
(9, 'EDPApp', 'login'),
(10, 'EDPApp', 'menu'),
(12, 'EDPApp', 'menustock'),
(11, 'EDPApp', 'menutype'),
(14, 'EDPApp', 'orderlist'),
(20, 'EDPApp', 'rating'),
(17, 'EDPApp', 'recommendation'),
(15, 'EDPApp', 'staff'),
(16, 'EDPApp', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'EDPApp', '0001_initial', '2025-02-11 08:24:32.729382'),
(2, 'contenttypes', '0001_initial', '2025-02-11 08:24:32.779438'),
(3, 'auth', '0001_initial', '2025-02-11 08:24:33.145050'),
(4, 'admin', '0001_initial', '2025-02-11 08:24:33.224610'),
(5, 'admin', '0002_logentry_remove_auto_add', '2025-02-11 08:24:33.229117'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-11 08:24:33.240395'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-02-11 08:24:33.298895'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-02-11 08:24:33.359161'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-02-11 08:24:33.371418'),
(10, 'auth', '0004_alter_user_username_opts', '2025-02-11 08:24:33.374927'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-02-11 08:24:33.439157'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-02-11 08:24:33.439157'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-02-11 08:24:33.456073'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-02-11 08:24:33.462969'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-02-11 08:24:33.469076'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-02-11 08:24:33.479014'),
(17, 'auth', '0011_update_proxy_permissions', '2025-02-11 08:24:33.489118'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-02-11 08:24:33.499234'),
(19, 'sessions', '0001_initial', '2025-02-11 08:24:33.519024'),
(20, 'EDPApp', '0002_complaint_status', '2025-02-12 07:15:58.860858'),
(21, 'EDPApp', '0003_complaint_completion_date', '2025-02-12 08:37:18.362212'),
(22, 'EDPApp', '0004_complaint_assigned_date_and_more', '2025-02-12 09:22:51.721901'),
(23, 'EDPApp', '0005_rating', '2025-02-12 10:44:14.610543'),
(24, 'EDPApp', '0006_alter_complaint_assigned_date_and_more', '2025-02-12 12:29:05.644809'),
(25, 'EDPApp', '0007_rename_completion_date_complaint_completed_date_and_more', '2025-02-12 18:24:19.509089'),
(26, 'EDPApp', '0008_delete_recommendation', '2025-02-14 06:19:44.828581');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('gywpa5nvhatnro1tr0oownspzy59i6dc', 'eyJ1c2VybmFtZSI6ImFqdTEyMzQiLCJyb2xlIjoic3RhZmYiLCJpZCI6Mn0:1thsud:_AMQkHYzXDqUphlR4FJISMRoWsR6_scW9kmAp_kLdG0', '2025-02-25 16:15:03.248728'),
('ric0rbj0cfydqd578xh92c40jwsrut49', '.eJyrViotTi3KS8xNVbJSSkzJzcxT0lEqys9B5mamKFkZ1gIAMM4NdQ:1tiHKi:HQys_vDgvW4KFBzZESRwurIQAkhCRUPYG8rt37zx5D0', '2025-02-26 18:19:36.132531'),
('xpuwww75c576t02tki63e5efnle2o9yj', 'e30:1tjFZJ:Hhvz3U9VHY2DlLgprRmIO2_b2RSo1QUOlhJzeGARK8Y', '2025-03-01 10:38:41.345224');

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_amc`
--

CREATE TABLE `edpapp_amc` (
  `amc_id` int(11) NOT NULL,
  `amc_from` varchar(100) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `amc_to` varchar(100) NOT NULL,
  `amc_amount` varchar(500) NOT NULL,
  `amc_status` varchar(100) NOT NULL,
  `User_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_bill`
--

CREATE TABLE `edpapp_bill` (
  `billno` int(11) NOT NULL,
  `date` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `order_status` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_bill`
--

INSERT INTO `edpapp_bill` (`billno`, `date`, `total`, `order_status`, `user_id`) VALUES
(1, '2025-02-11', '71700', 'waiting', 1),
(2, '2025-02-11', '120000', 'waiting', 1);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_cart`
--

CREATE TABLE `edpapp_cart` (
  `cart_id` int(11) NOT NULL,
  `pqty` varchar(100) NOT NULL,
  `cart_date` varchar(100) NOT NULL,
  `cart_status` varchar(100) NOT NULL,
  `menu_id_id` int(11) DEFAULT NULL,
  `stock_id_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_cart`
--

INSERT INTO `edpapp_cart` (`cart_id`, `pqty`, `cart_date`, `cart_status`, `menu_id_id`, `stock_id_id`, `user_id`) VALUES
(1, '1', '2025-02-11', 'approved', 1, 1, 1),
(2, '1', '2025-02-11', 'approved', 3, 2, 1),
(3, '1', '2025-02-11', 'approved', 4, 3, 1),
(4, '1', '2025-02-11', 'approved', 2, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_chat`
--

CREATE TABLE `edpapp_chat` (
  `chat_id` int(11) NOT NULL,
  `chat_message` varchar(150) NOT NULL,
  `chat_date` datetime(6) NOT NULL,
  `chat_first_person_login_id` int(11) NOT NULL,
  `chat_second_person_login_id` int(11) NOT NULL,
  `chat_user` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_chat`
--

INSERT INTO `edpapp_chat` (`chat_id`, `chat_message`, `chat_date`, `chat_first_person_login_id`, `chat_second_person_login_id`, `chat_user`) VALUES
(1, 'hi', '2025-02-11 21:16:59.583984', 3, 0, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_complaint`
--

CREATE TABLE `edpapp_complaint` (
  `Complaint_id` int(11) NOT NULL,
  `Complaint_subject` varchar(100) NOT NULL,
  `Complaint_message` varchar(500) NOT NULL,
  `Complaint_date` varchar(100) NOT NULL,
  `Complaint_reply` varchar(500) NOT NULL,
  `Complaint_priority` varchar(100) DEFAULT NULL,
  `Complaint_product` varchar(100) DEFAULT NULL,
  `allot_id_id` int(11) DEFAULT NULL,
  `User_id_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `completed_date` date DEFAULT NULL,
  `assigned_date` date DEFAULT NULL,
  `deadline_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_complaint`
--

INSERT INTO `edpapp_complaint` (`Complaint_id`, `Complaint_subject`, `Complaint_message`, `Complaint_date`, `Complaint_reply`, `Complaint_priority`, `Complaint_product`, `allot_id_id`, `User_id_id`, `status`, `completed_date`, `assigned_date`, `deadline_date`) VALUES
(1, 'Request for Support – Lenovo i5 Laptop Not Working Properly', 'I am writing to request technical assistance for my Lenovo i5 laptop, which is not functioning properly. ', '2025-02-11', 'Yes', 'HIGH', 'Model: [Your Laptop Model]\r\nSerial Number: [Your Serial Number]\r\nOperating System: [Windows 10/11, e', 1, 1, 'Completed', '2025-02-19', '2025-02-12', '2025-02-20'),
(2, 'Request for Support – Lenovo i5 Laptop Not Working Properly', 'I am writing to request technical assistance for my Lenovo i5 laptop, which is not functioning properly. ', '2025-02-11', 'Gud', 'HIGH', 'Model: [Your Laptop Model]\r\nSerial Number: [Your Serial Number]\r\nOperating System: [Windows 10/11, e', 1, 1, NULL, NULL, '2025-02-12', '2025-02-20'),
(3, 'dsfds', 'sdfsdf', '2025-02-11', 'not yet Seen', 'LOW', 'dsfsdf', 1, 1, NULL, NULL, '2025-02-12', '2025-02-20'),
(4, 'Jamesfdgfdf', 'fgfdg', '2025-02-12', 'dsfsdf', 'LOW', 'fdgfd', 2, 1, 'Completed', '2025-02-21', '2025-02-12', '2025-02-19'),
(5, 'dfsdf', 'dsfds', '2025-02-12', 'not yet Seen', 'MEDIUM', 'dsfds', 2, 1, 'Pending', NULL, '2025-02-15', '2025-02-19');

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_login`
--

CREATE TABLE `edpapp_login` (
  `log_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_login`
--

INSERT INTO `edpapp_login` (`log_id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin', 'admin'),
(2, 'aju1234', 'aju1234', 'staff'),
(3, 'james23', 'james23', 'user'),
(4, 'jithin123', 'jithin123', 'staff'),
(5, 'sam123', 'sam123', 'staff');

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_menu`
--

CREATE TABLE `edpapp_menu` (
  `menu_id` int(11) NOT NULL,
  `menu_name` varchar(100) NOT NULL,
  `menu_price` varchar(100) NOT NULL,
  `menu_photo` varchar(1000) NOT NULL,
  `menu_type_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_menu`
--

INSERT INTO `edpapp_menu` (`menu_id`, `menu_name`, `menu_price`, `menu_photo`, `menu_type_id`) VALUES
(1, 'Lenovo i5 ideapad', '70000', 'images/Cpter1.jpg', 1),
(2, 'Lenovo i7 ideapad', '120000', 'images/ctr3.jpg', 1),
(3, 'Portronics Harmonics S16 ', '700', 'images/e1.jpg', 4),
(4, 'Zebronics Zeb-Rise Wired Optical Mouse', '1000', 'images/m1.jpg', 2),
(5, 'Zebronics Zeb-200HM Wired', '1200', 'images/h2.jpg', 5);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_menustock`
--

CREATE TABLE `edpapp_menustock` (
  `stock_id` int(11) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `menu_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_menustock`
--

INSERT INTO `edpapp_menustock` (`stock_id`, `qty`, `date`, `menu_id_id`) VALUES
(1, '14', '2025-02-11', 1),
(2, '5', '2025-02-11', 3),
(3, '10', '2025-02-11', 4),
(4, '15', '2025-02-11', 5),
(5, '2', '2025-02-11', 2);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_menutype`
--

CREATE TABLE `edpapp_menutype` (
  `type_id` int(11) NOT NULL,
  `type_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_menutype`
--

INSERT INTO `edpapp_menutype` (`type_id`, `type_name`) VALUES
(1, 'Laptop'),
(2, 'Mouse'),
(3, 'Keyboard'),
(4, 'Ear Buds'),
(5, 'Head Set');

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_orderlist`
--

CREATE TABLE `edpapp_orderlist` (
  `orderno` int(11) NOT NULL,
  `billno_id` int(11) DEFAULT NULL,
  `cart_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_orderlist`
--

INSERT INTO `edpapp_orderlist` (`orderno`, `billno_id`, `cart_id_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_rating`
--

CREATE TABLE `edpapp_rating` (
  `rating_id` int(11) NOT NULL,
  `rating` decimal(5,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `Complaint_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_rating`
--

INSERT INTO `edpapp_rating` (`rating_id`, `rating`, `timestamp`, `Complaint_id_id`) VALUES
(1, 1.50, '2025-02-12 11:04:28.516957', 3),
(2, 2.50, '2025-02-12 11:05:17.500144', 2),
(3, 5.00, '2025-02-12 18:19:28.879578', 4);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_staff`
--

CREATE TABLE `edpapp_staff` (
  `Staff_id` int(11) NOT NULL,
  `Staff_name` varchar(100) NOT NULL,
  `Staff_address` varchar(500) NOT NULL,
  `Staff_email` varchar(200) NOT NULL,
  `Staff_phone` varchar(100) NOT NULL,
  `Staff_qualification` varchar(200) NOT NULL,
  `Staff_designation` varchar(100) NOT NULL,
  `Staff_experience` varchar(100) NOT NULL,
  `Staff_photo` varchar(1000) NOT NULL,
  `Staff_status` varchar(50) NOT NULL,
  `Staff_logid_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_staff`
--

INSERT INTO `edpapp_staff` (`Staff_id`, `Staff_name`, `Staff_address`, `Staff_email`, `Staff_phone`, `Staff_qualification`, `Staff_designation`, `Staff_experience`, `Staff_photo`, `Staff_status`, `Staff_logid_id`) VALUES
(1, 'Aju Thomas', 'Aju Villa', 'aju@gmail.com', '8965485256', 'SSLC,Plus two,UG,PG', 'Engineer', '6', '6..jpg', 'approved', 2),
(2, 'Jithin', 'Jithin Villa', 'jithin@gmail.com', '8596365241', 'SSLC,Plus two,UG,PG', 'Engineer', '3', '3..jpg', 'approved', 4),
(3, 'Sam Varghese', 'Sam Villa', 'sam@gmail.com', '9847569856', 'SSLC,Plus two,UG,PG', 'Hardware tech', '7', '2..jpg', 'approved', 5);

-- --------------------------------------------------------

--
-- Table structure for table `edpapp_user`
--

CREATE TABLE `edpapp_user` (
  `User_id` int(11) NOT NULL,
  `User_name` varchar(200) NOT NULL,
  `User_address` varchar(200) NOT NULL,
  `User_email` varchar(100) NOT NULL,
  `User_phone` varchar(100) NOT NULL,
  `User_alt_No` varchar(200) NOT NULL,
  `User_status` varchar(200) NOT NULL,
  `Log_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edpapp_user`
--

INSERT INTO `edpapp_user` (`User_id`, `User_name`, `User_address`, `User_email`, `User_phone`, `User_alt_No`, `User_status`, `Log_id_id`) VALUES
(1, 'James', 'James Villa', 'james@gmail.com', '9865321245', '7485965465', 'approved', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `edpapp_amc`
--
ALTER TABLE `edpapp_amc`
  ADD PRIMARY KEY (`amc_id`),
  ADD KEY `EDPApp_amc_User_id_id_319cee3d_fk_EDPApp_user_User_id` (`User_id_id`);

--
-- Indexes for table `edpapp_bill`
--
ALTER TABLE `edpapp_bill`
  ADD PRIMARY KEY (`billno`),
  ADD KEY `EDPApp_bill_user_id_492ea1fa_fk_EDPApp_user_User_id` (`user_id`);

--
-- Indexes for table `edpapp_cart`
--
ALTER TABLE `edpapp_cart`
  ADD PRIMARY KEY (`cart_id`),
  ADD KEY `EDPApp_cart_user_id_897c7cd0_fk_EDPApp_user_User_id` (`user_id`),
  ADD KEY `EDPApp_cart_menu_id_id_7744ffb6_fk_EDPApp_menu_menu_id` (`menu_id_id`),
  ADD KEY `EDPApp_cart_stock_id_id_8f1f9b08_fk_EDPApp_menustock_stock_id` (`stock_id_id`);

--
-- Indexes for table `edpapp_chat`
--
ALTER TABLE `edpapp_chat`
  ADD PRIMARY KEY (`chat_id`);

--
-- Indexes for table `edpapp_complaint`
--
ALTER TABLE `edpapp_complaint`
  ADD PRIMARY KEY (`Complaint_id`),
  ADD KEY `EDPApp_complaint_allot_id_id_9874334d_fk_EDPApp_staff_Staff_id` (`allot_id_id`),
  ADD KEY `EDPApp_complaint_User_id_id_85299a77_fk_EDPApp_user_User_id` (`User_id_id`);

--
-- Indexes for table `edpapp_login`
--
ALTER TABLE `edpapp_login`
  ADD PRIMARY KEY (`log_id`);

--
-- Indexes for table `edpapp_menu`
--
ALTER TABLE `edpapp_menu`
  ADD PRIMARY KEY (`menu_id`),
  ADD KEY `EDPApp_menu_menu_type_id_5b61a562_fk_EDPApp_menutype_type_id` (`menu_type_id`);

--
-- Indexes for table `edpapp_menustock`
--
ALTER TABLE `edpapp_menustock`
  ADD PRIMARY KEY (`stock_id`),
  ADD KEY `EDPApp_menustock_menu_id_id_ba61cc91_fk_EDPApp_menu_menu_id` (`menu_id_id`);

--
-- Indexes for table `edpapp_menutype`
--
ALTER TABLE `edpapp_menutype`
  ADD PRIMARY KEY (`type_id`);

--
-- Indexes for table `edpapp_orderlist`
--
ALTER TABLE `edpapp_orderlist`
  ADD PRIMARY KEY (`orderno`),
  ADD KEY `EDPApp_orderlist_billno_id_0672130b_fk_EDPApp_bill_billno` (`billno_id`),
  ADD KEY `EDPApp_orderlist_cart_id_id_73015c97_fk_EDPApp_cart_cart_id` (`cart_id_id`);

--
-- Indexes for table `edpapp_rating`
--
ALTER TABLE `edpapp_rating`
  ADD PRIMARY KEY (`rating_id`),
  ADD KEY `EDPApp_rating_Complaint_id_id_3cbc0aa6_fk_EDPApp_co` (`Complaint_id_id`);

--
-- Indexes for table `edpapp_staff`
--
ALTER TABLE `edpapp_staff`
  ADD PRIMARY KEY (`Staff_id`),
  ADD KEY `EDPApp_staff_Staff_logid_id_f66e6db8_fk_EDPApp_login_log_id` (`Staff_logid_id`);

--
-- Indexes for table `edpapp_user`
--
ALTER TABLE `edpapp_user`
  ADD PRIMARY KEY (`User_id`),
  ADD KEY `EDPApp_user_Log_id_id_e59d12bf_fk_EDPApp_login_log_id` (`Log_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `edpapp_amc`
--
ALTER TABLE `edpapp_amc`
  MODIFY `amc_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `edpapp_bill`
--
ALTER TABLE `edpapp_bill`
  MODIFY `billno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `edpapp_cart`
--
ALTER TABLE `edpapp_cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `edpapp_chat`
--
ALTER TABLE `edpapp_chat`
  MODIFY `chat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `edpapp_complaint`
--
ALTER TABLE `edpapp_complaint`
  MODIFY `Complaint_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `edpapp_login`
--
ALTER TABLE `edpapp_login`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `edpapp_menu`
--
ALTER TABLE `edpapp_menu`
  MODIFY `menu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `edpapp_menustock`
--
ALTER TABLE `edpapp_menustock`
  MODIFY `stock_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `edpapp_menutype`
--
ALTER TABLE `edpapp_menutype`
  MODIFY `type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `edpapp_orderlist`
--
ALTER TABLE `edpapp_orderlist`
  MODIFY `orderno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `edpapp_rating`
--
ALTER TABLE `edpapp_rating`
  MODIFY `rating_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `edpapp_staff`
--
ALTER TABLE `edpapp_staff`
  MODIFY `Staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `edpapp_user`
--
ALTER TABLE `edpapp_user`
  MODIFY `User_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `edpapp_amc`
--
ALTER TABLE `edpapp_amc`
  ADD CONSTRAINT `EDPApp_amc_User_id_id_319cee3d_fk_EDPApp_user_User_id` FOREIGN KEY (`User_id_id`) REFERENCES `edpapp_user` (`User_id`);

--
-- Constraints for table `edpapp_bill`
--
ALTER TABLE `edpapp_bill`
  ADD CONSTRAINT `EDPApp_bill_user_id_492ea1fa_fk_EDPApp_user_User_id` FOREIGN KEY (`user_id`) REFERENCES `edpapp_user` (`User_id`);

--
-- Constraints for table `edpapp_cart`
--
ALTER TABLE `edpapp_cart`
  ADD CONSTRAINT `EDPApp_cart_menu_id_id_7744ffb6_fk_EDPApp_menu_menu_id` FOREIGN KEY (`menu_id_id`) REFERENCES `edpapp_menu` (`menu_id`),
  ADD CONSTRAINT `EDPApp_cart_stock_id_id_8f1f9b08_fk_EDPApp_menustock_stock_id` FOREIGN KEY (`stock_id_id`) REFERENCES `edpapp_menustock` (`stock_id`),
  ADD CONSTRAINT `EDPApp_cart_user_id_897c7cd0_fk_EDPApp_user_User_id` FOREIGN KEY (`user_id`) REFERENCES `edpapp_user` (`User_id`);

--
-- Constraints for table `edpapp_complaint`
--
ALTER TABLE `edpapp_complaint`
  ADD CONSTRAINT `EDPApp_complaint_User_id_id_85299a77_fk_EDPApp_user_User_id` FOREIGN KEY (`User_id_id`) REFERENCES `edpapp_user` (`User_id`),
  ADD CONSTRAINT `EDPApp_complaint_allot_id_id_9874334d_fk_EDPApp_staff_Staff_id` FOREIGN KEY (`allot_id_id`) REFERENCES `edpapp_staff` (`Staff_id`);

--
-- Constraints for table `edpapp_menu`
--
ALTER TABLE `edpapp_menu`
  ADD CONSTRAINT `EDPApp_menu_menu_type_id_5b61a562_fk_EDPApp_menutype_type_id` FOREIGN KEY (`menu_type_id`) REFERENCES `edpapp_menutype` (`type_id`);

--
-- Constraints for table `edpapp_menustock`
--
ALTER TABLE `edpapp_menustock`
  ADD CONSTRAINT `EDPApp_menustock_menu_id_id_ba61cc91_fk_EDPApp_menu_menu_id` FOREIGN KEY (`menu_id_id`) REFERENCES `edpapp_menu` (`menu_id`);

--
-- Constraints for table `edpapp_orderlist`
--
ALTER TABLE `edpapp_orderlist`
  ADD CONSTRAINT `EDPApp_orderlist_billno_id_0672130b_fk_EDPApp_bill_billno` FOREIGN KEY (`billno_id`) REFERENCES `edpapp_bill` (`billno`),
  ADD CONSTRAINT `EDPApp_orderlist_cart_id_id_73015c97_fk_EDPApp_cart_cart_id` FOREIGN KEY (`cart_id_id`) REFERENCES `edpapp_cart` (`cart_id`);

--
-- Constraints for table `edpapp_rating`
--
ALTER TABLE `edpapp_rating`
  ADD CONSTRAINT `EDPApp_rating_Complaint_id_id_3cbc0aa6_fk_EDPApp_co` FOREIGN KEY (`Complaint_id_id`) REFERENCES `edpapp_complaint` (`Complaint_id`);

--
-- Constraints for table `edpapp_staff`
--
ALTER TABLE `edpapp_staff`
  ADD CONSTRAINT `EDPApp_staff_Staff_logid_id_f66e6db8_fk_EDPApp_login_log_id` FOREIGN KEY (`Staff_logid_id`) REFERENCES `edpapp_login` (`log_id`);

--
-- Constraints for table `edpapp_user`
--
ALTER TABLE `edpapp_user`
  ADD CONSTRAINT `EDPApp_user_Log_id_id_e59d12bf_fk_EDPApp_login_log_id` FOREIGN KEY (`Log_id_id`) REFERENCES `edpapp_login` (`log_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
